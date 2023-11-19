from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import render
def user_has_designation(designation):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user has the specified designation
            if request.user.is_authenticated and hasattr(request.user, 'customuserprofile'):
                user_designation = request.user.customuserprofile.designation
                if user_designation == designation:
                    return view_func(request, *args, **kwargs)
            # If the user doesn't have the correct designation, you can redirect them or show an error page
            return render(request, 'base/access_denied.html', status=403)
        return _wrapped_view
    return decorator
