#
#
# class ServiceVersion:
#
#
#     serialVersionUID = 1
#
#
#     id;
# / ** 版本号 * /
#      private
# String
# versionNo;
# / ** 版本名称 * /
#      private
# String
# versionName;
# / ** 版本内容 * /
#      private
# String
# versionContent;
# / ** 版本类型1、前端；2、后台 * /
#                 private
# String
# versionType;
#
# public
# ServiceVersion()
# {
# }
#
# public
# ServiceVersion(String
# versionType) {
#     this.versionType = versionType;
# }
#
# public
# void
# setId(Integer
# id){
#     this.id = id;
# }
#
# public
# Integer
# getId()
# {
# return id;
# }
# public
# void
# setVersionNo(String
# versionNo){
# this.versionNo = versionNo;
# }
#
# public
# String
# getVersionNo()
# {
# return versionNo;
# }
# public
# void
# setVersionName(String
# versionName){
# this.versionName = versionName;
# }
#
# public
# String
# getVersionName()
# {
# return versionName;
# }
# public
# void
# setVersionContent(String
# versionContent){
# this.versionContent = versionContent;
# }
#
# public
# String
# getVersionContent()
# {
# return versionContent;
# }
# public
# void
# setVersionType(String
# versionType){
# this.versionType = versionType;
# }
#
# public
# String
# getVersionType()
# {
# return versionType;
# }
#
# public
# String
# toString()
# {
# return new
# ToStringBuilder(this, ToStringStyle.MULTI_LINE_STYLE)
# .append("id", getId())
# .append("versionNo", getVersionNo())
# .append("versionName", getVersionName())
# .append("versionContent", getVersionContent())
# .append("versionType", getVersionType())
# .append("isDel", getIsDel())
# .append("createBy", getCreateBy())
# .append("createTime", getCreateTime())
# .append("updateBy", getUpdateBy())
# .append("updateTime", getUpdateTime())
# .append("remark", getRemark())
# .toString();
# }
# }