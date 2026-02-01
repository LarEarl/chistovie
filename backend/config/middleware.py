from django.conf import settings


class CORSMediaMiddleware:
    """Добавляет CORS headers для media файлов"""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if this is a media file request
        if request.path.startswith('/media/'):
            origin = request.headers.get('Origin')
            
            # Check if origin is allowed
            if origin and origin in settings.CORS_ALLOWED_ORIGINS:
                response['Access-Control-Allow-Origin'] = origin
                response['Access-Control-Allow-Credentials'] = 'true'
                response['Access-Control-Allow-Methods'] = 'GET, HEAD, OPTIONS'
                response['Access-Control-Allow-Headers'] = 'Content-Type'
        
        return response
