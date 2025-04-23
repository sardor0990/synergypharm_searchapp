class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split('.')[0]
        
        if host == 'start':
            request.urlconf = 'start.urls'
        elif host == 'lists':
            request.urlconf = 'people.urls'  # Must match your app name
            
        return self.get_response(request)