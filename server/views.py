from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def Message(request):
    '''
    returns the message for demo
    '''
    d1 = {'message': 'Hello Fabl'}
    return Response(d1)
