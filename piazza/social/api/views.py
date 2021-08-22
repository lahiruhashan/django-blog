from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import permission_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from social.api.serializers import PostSerializer
from social.models import Post


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def post_list(request):
    if request.method == 'GET':
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        response = {"status": "Not Found"}
        return JsonResponse(response, status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)


@api_view(['PUT', ])
@permission_classes([IsAuthenticated])
def update_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        response = {"status": "Not Found"}
        return JsonResponse(response, status=404)

    user = request.user
    if post.author != user:
        return JsonResponse({'response': "You do not have permission to edit this post"})

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        response = {}
        if serializer.is_valid():
            serializer.save()
            response["success"] = "update successful"
            return JsonResponse(response)
        return JsonResponse(serializer.errors, status=400)


@api_view(['DELETE', ])
@permission_classes([IsAuthenticated])
def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    user = request.user
    if post.author != user:
        return JsonResponse({'response': "You do not have permission to delete this post"})

    if request.method == 'DELETE':
        operation = post.delete()
        response = {}
        if operation:
            response["success"] = "delete successful"
        else:
            response["failed"] = "delete failed"
        return JsonResponse(response)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_post(request):
    account = request.user
    post = Post(author=account)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        response = {}
        if serializer.is_valid():
            serializer.save()
            response["success"] = "post created successful"
            response["post"] = serializer.data
            return JsonResponse(response, status=201)
        return JsonResponse(serializer.errors, status=400)
