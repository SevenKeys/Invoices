from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.models import User


# mixin so that only registered users can have access
class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


# mixin so that users can have access data their company only
# class CompanyFilterMixin(object):
# 	def __init__(self):
# 		self.user = User.objects.get(name=self.request.user)
# 		self.company = self.user.company

# 	def get_queryset(self):
# 		return super(CompanyFilterMixin,self).get_queryset().filter(company=self.company)
