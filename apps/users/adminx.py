from users.models import Member
from xadmin import views
import xadmin

class BaseSetting(object):
    '''
    主题样式多样化
    '''
    enable_themes=True
    use_bootswatch=True

xadmin.site.register(views.BaseAdminView,BaseSetting)

class GlobalSetting(object):
    #页头
    site_title = '案场渠道稽核管理系统'
    #页脚
    site_footer = '深圳文达智通技术有限公司'

class MemberAdmin(object):
    list_display=('user','name','nodes')
    search_fields=('nodes',)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Member,MemberAdmin)
