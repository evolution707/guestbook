from django.shortcuts import render,redirect,HttpResponse
from guest_book import models
from .forms import GuestForm
import json

def guestbook(request,pid):
    
    if request.method == 'GET':
        if pid == None:
            pid = 1
        current_page = int(pid)
        # 起始索引，（当前页码-1）* 每页显示条数
        start = (current_page - 1) * 10
        end = current_page * 10
        # 从数据库取值的范围
        guest_list = models.GuestBook.objects.all()[start:end]
        total_count = models.GuestBook.objects.all().count()
        # 总条数除以每页显示10条，得到页数，余数不等于0，另起一页
        total_page, a = divmod(total_count, 10)
        if a != 0:
            total_page += 1

        # 显示的页码数
        page_list = []
        # 如果当前页为第一页，上一页则不再跳转
        if current_page == 1:
            page_list.append("<a href='javascript:void(0);' style='text-decoration:none'><上一页</a>")
        else:
            page_list.append("<a href='/guestbook/%s'><上一页</a>"% (current_page - 1, ))

        global page_start,page_end
        if total_page <= 11:
            page_start = 1
            page_end = total_page
        else :
            if current_page <= 6:
                page_start = 1
                page_end = 11 + 1
            elif current_page > 6:
                # 生成首页 和 ...
                page_list.append("<a href='/guestbook/%s'>1</a>" % (1,))
                page_list.append("<a href='javascript:void(0);'>...</a>")

                if total_page - current_page >= 5:
                    page_start = current_page - 3
                    page_end = current_page + 4
                else:
                    page_start = total_page - 8
                    page_end = total_page + 1

                # 接上，最后一页为当前页+6，但不能让他一直+6，当最后一页的页码数大于最大页码数时，让最后一页变成当前页，不再加了
                if page_end >= total_page:
                    page_end = current_page + 1
                if current_page + 5 >= total_page:
                    page_end = total_page + 1

            # 根据不同的起始页和终止页生成相应的页码
            for page in range(page_start, page_end):
                # 当前页增加样式
                if page == current_page:
                    page_list.append("<a class='active' href='/guestbook/%s'>%s</a>"% (page, page))
                else:
                    page_list.append("<a href='/guestbook/%s'>%s</a>"% (page, page))
            # 生成 ... 和 尾页
            if current_page > 6 and (total_page - current_page >= 6):
                page_list.append("<a href='javascript:void(0);'>...</a>")
                page_list.append("<a href='/guestbook/%s'>%s</a>" % (total_page, total_page))

            # 如果当前页为总页数，下一页则不再跳转
            if current_page == total_page:
                page_list.append("<a href='javascript:void(0);' style='text-decoration:none'>下一页></a>")
            else:
                page_list.append("<a href='/guestbook/%s'>下一页></a>" % (current_page + 1,))

            page_list = ''.join(page_list)

        return render(request,'guestbook.html',{'guest_list':guest_list,'total_count':total_count, 'page_list':page_list})

    elif request.method == "POST":
        ret = {'status': True, 'error': None, 'data': None}
        obj = GuestForm(request.POST)
        if obj.is_valid():
            models.GuestBook.objects.create(**obj.cleaned_data)
           
            # 生成测试数据
#             for i in range(500):
#                 models.GuestBook.objects.create(username= str(i),
#                                                content= str(i))
            
        else:
            res_str = obj.errors.as_json()  # res_str是一个字符串
            ret['status'] = False
            ret['error'] = res_str
        return HttpResponse(json.dumps(ret))



