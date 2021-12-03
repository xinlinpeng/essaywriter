from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from . import write_text
import time
import sys
import traceback
import random
from . import database

# from .models import Book


# Create your views here.
@require_http_methods(["GET"])
def write_para(request):
    response = {}
    try:
        # book = Book(book_name=request.GET.get('book_name'))
        # book.save()
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        topic = request.GET.get('topic')
        keyword_list = request.GET.get('keyword')
        keyword = []
        result = ""
        e = ""
        e_msg = ""
        if keyword_list != None and keyword_list != "":
            keyword = keyword_list.split(' ')
        if topic != None and topic != "":
            if topic == "1失败是成功之母。":
                result = ""
            #     result = "失败是成功之母。如果你能抛开过去,并且从现在开始更好地做,你就有可能成功,做对未来有益的尝试。击退失败的方法，可以有效地改变自己，培养自己的技能。失败是获得成功的最好机会。如果能在失败中学习并成长成熟，将能成为一个勇敢的人。如果能在失败中学习且成长成熟，那么，你就能拥有成功。你可以从失败的教训中收获更多的东西，这样的收获甚至比已有成功还要多。不需要昂贵的投资，也不需要再努力去做一些务虚的工作。正如失败仅仅是成功的一部分一样，失败也仅是成功之母。"
            # elif topic == "2失败是成功之母。":
            #     result = "失败是成功之母。失败往往是成功的前奏,失败是成功之母。当我们好不容易奋斗走向成功时,在取得最后胜利的喜悦中,往往会出现“人生若只如初见”的现象。古人云:“人生不如意事十有八九”;“天下不如意事常八九”。这一生活哲理对我们今天的人来说,有其重要的教育意义。谁愿意一帆风顺,平步青云,谁不愿意失败、挫折、失落、痛苦失败是成功之母。当我们好不容易奋斗走向成功时,在取得最后胜利的喜悦中,往往会出现“人生若只如初见”的现象。"
            # elif topic == "1通过失败积攒的经验,最终会成为走向成功的基石。":
            #     result = "通过失败积攒的经验,最终会成为走向成功的基石。失败并不可怕,因为失败当中存在着成功的契机。在这个世界上没有任何人、任何事是完全完美的,甚至没有人比我们自己更了解自己。走好每一天,就意味你是在为明天积蓄力量,蓄积值得你信赖的力量。失败并不可怕，因为失败当中存在着成功的契机。在这个世界上没有任何人、任何事是完全完美的，甚至没有人比我们自己更了解自己。走好每一天，就意味你是在为明天积蓄力量，蓄积值得你信赖的力量。"
            # elif topic == "2通过失败积攒的经验,最终会成为走向成功的基石。":
            #     result = "通过失败积攒的经验,最终会成为走向成功的基石。 自我开发能力是智商,创新能力是情商,社交能力是逆商。 懂得失败是走向成功的基石。自作聪明会让自己离成功越来越远。 失败是上帝送给每个人最好的礼物,让我们在自卑和自信间徘徊,在压抑和轻松中徘徊,在痛苦和快乐中徘徊,在发呆和疯狂中徘徊。如果一个人整天无所事事,就会经常胡思乱想,就会觉得时间没有目标没有意义,就会茫然失措,就会心急如焚,就会焦虑,就会自责。我们不能永远保持理智和清醒。失败是人生在世的常态,愿我们亲历失败,在失败中锤炼自己,从失败中找寻成功的方法。"
            # elif topic == "1正确看待成功与失败,不要因为成功自满,也不要因为失败气馁。":
            #     result = "正确看待成功与失败,不要因为成功自满,也不要因为失败气馁。全书围绕“成功”、“成功者的特质”、“成功之路”、“聪明与智慧”等25个主题,对成功与失败的原因、影响、如何走出失败的迷途等方面进行了深刻探讨,以帮助读者重新认识成功,把握投资自己、奋斗目标的正确走向。孔子云，“知耻近乎勇”。《左传》对这句话作了补充，将其解释为“知耻近乎仁”。失败使很多人失去了热情、信心，这是十分可怕的。失败使人灰心丧气，不思进取。成功，是对失败的超越!改变“半途而废”的坏习惯;学会引导自己走向成功之路。常思失败原因，失败并不是成功的大敌，而成功才是真正的敌人。成功者既要肯于面对失败，更要善于走出失败的误区。"
            # elif topic == "2正确看待成功与失败,不要因为成功自满,也不要因为失败气馁。":
            #     result = "正确看待成功与失败,不要因为成功自满,也不要因为失败气馁。成功与失败是每个人都无法回避的,在所有困境之中,人的认知是最为重要的。成功需要你去充分地认知,而失败又何尝不是你想避免的呢。在无数次失败的教训中,成功与失败了。如何面对成功和失败,也是一直以来萦绕着很多人的一个问题。有专家甚至认为，幸福是主体必须追求的目标之一。如果没有了理想，幸福也就只能沦为一种空谈。然而，在肉体的幸福和精神幸福的多种多样中，其追求目标多么丰富啊!失败就足以表明，我们拥有无限的力量去追求理想和幸福。成功与失败，舍弃中间的一条缝，追寻极致的悲剧和喜剧，就会变得更加真实。成功与失败真得没有那么可怕，也并不那么神秘。成功与失败之间真实存在着一条非常微妙的缝隙，尽管每一件成功之事都有其幸运的一面。但这并不意味着中间有一条缝，一不留神就会掉进沟里。人们往往会在失败中感悟到一条道路，在挫折和困难之中寻找希望和光明。"
            else:
                gene_type = "chat&qa"
                get_num = write_text.get_num()
                if get_num["quota"]["chat"] < 10 or get_num["quota"]["qa"] < 10:
                    response['msg'] = 'chat:'+str(get_num["quota"]["chat"])+" qa:"+str(get_num["quota"]["qa"])
                    response["error_num"] = 2
                else:
                    write_type = "mixed"
                    if random.randint(0,2) == 0:
                        tmp = write_text.write_para(topic,keyword,200)
                    else:
                        write_type = "chat"
                        gene_type = "chat"
                        tmp = write_text.write_para_chat(topic,keyword,200)
                    result = tmp
                    response['msg'] = 'success'
                    response['error_num'] = 0
                    response["ret_val"] = tmp
                    response["write_type"] = write_type
                finish_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                
                database.save_cache(topic,start_time,finish_time,gene_type,keyword_list,result)
                    # if e != "":
                    #     response['e'] = e
                    #     response['e_msg'] = e_msg
        response['topic'] = str(topic)
        response['keyword'] = str(keyword_list)
        response['result'] = result
    except  Exception as e:
        response['msg'] = traceback.format_exc()
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        # books = Book.objects.filter()
        # response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def get_recent_time(request):
    response = {}
    try:
        # books = Book.objects.filter()
        # response['list'] = json.loads(serializers.serialize("json", books))
        res = database.get_recent_time()
        response['msg'] = 'success'
        response['error_num'] = 0
        response['min'] = res['min']
        response['max'] = res['max']
        response['avg'] = res['avg']
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def get_cache_by_id(request):
    response = {}
    try:
        # books = Book.objects.filter()
        # response['list'] = json.loads(serializers.serialize("json", books))
        id = int(request.GET.get('id'))
        result = database.search_by_id(id)
        if len(result) == 0:
            response['msg'] = "id didn't find, id = "+str(id)
            response['error_num'] = 1
        else:
            response['msg'] = 'success'
            response['error_num'] = 0
            topic = result[0]["topic"]
            keyword = result[0]["keywords"]
            para = result[0]["para"]
            para = write_text.del_unfinished(para)
            response['topic'] = topic
            response['keyword'] = keyword
            response['result'] = para
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)