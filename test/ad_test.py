#coding=utf-8

import sys
sys.path.append('..')
from ad_identify import AdIdentify

def main():
    msg={'author':u'蒲公英情感' ,'content':'李老汉是个外村人，十年前才搬到杨家村定居。当年李老汉相中一块好地，想在那里盖房子，可是村长就是不允许。后来，李老汉把村长灌醉后才清楚，那个地方原来是一个大户人家的祖坟，后来被仇家推平了。由于是坟地，风水不好，所以村里没人在那里盖房子，不吉利。 李老汉哪信这个，他就知道，地好，还没人抢，于是就强行跟村长要下了那块地，盖起了房子。村里人本来都不放心，可是李老汉在那里一住就是十年，一直平平安安，村里人都说是李老汉命硬，百鬼不侵。\n 李老汉家里养了一条大黑猎狗，平时就喜欢带着狗上山抓兔子。说也奇怪，每次黑狗都能抓到一只肥硕的兔子，摇着尾巴把兔子送到主人面前。李老汉通常都会把兔子脑袋给大黑狗吃，表示奖励。 十年后，李老汉老了，猎狗也老了，再也跑不动了，抓不到兔子了。对此，李老汉非常生气，他已经半个月没开荤腥了，嘴馋得厉害。\n一日喝完酒以后，把黑狗叫到旁边，拿着砍柴刀就用力砍到了老狗的脑袋上，老狗瞪大双眼，随后流出了眼泪，不敢相信自己的主人会突然杀死自己。 老狗死后，李老汉剥了狗皮，做了一大锅狗肉汤，吃的肚满肠肥，就躺在炕上沉沉睡去了。\n 半夜的时候，就感觉地动山摇，之后李老汉眼前一黑就没了知觉，死掉了。 次日，村民们发现李老汉家的房子塌了。就告诉了村长，村长带着村民过来救人。等到了以后，村民看到看见整个屋子阴气缭绕，好像有无数的冤魂恶鬼。村长看了眼墙根，发现老狗的狗皮完整的扔在了地上，村长这才知道，真正镇得住这些鬼魂的是大黑狗，而不是李老汉命硬。而李老汉居然吃了为自己效力多年的老狗，实在是让人心寒。\n 老狗死了，鬼魂自然害死了李老汉。再看一眼这完全倒塌的房子，就像一个活棺材，李老汉肯定被压死了，于是村长赶紧阻止大家施救，带着村民赶紧离开了这个不祥之地。\n 正所谓:善恶到头终有报，多行善事福满堂，多行恶事必遭殃。万物皆有灵性，对于李老汉这种，过河拆桥，兔死狗烹，忘恩负义的人，一点也不值得人同情。\n (图片源自网络，本文纯属虚构，弘扬正能量，多行善事。)' ,'url':'http://k.sina.com.cn/article_6524967235_184eb194300100d87n.html'}

    msg={'author':u'龙宝育儿说事','content':'一个被管制太多的孩子，他会逐渐从权威家长手下的“听差”，变成自身坏习惯的“奴隶”；他的坏习惯正是束缚他的、让他痛苦的桎梏。不是他心理不想摆脱，是他没有能力摆脱。 \n“第一反抗期”、“青春逆反期”等等这类说法，它是一种对儿童成长中正常行为的负面描述，是幼稚认识的产物，很容易误导一些家长。孩子从来没有反抗期，也没有逆反期，儿童的本性都非常温和。\n如果说他们有逆反，那是因为受到了压抑，或不被理解，一定是孩子家长平时对孩子有太多的管制，以至于让孩子不得不反抗了。\n这个年龄段的孩子对一切都充满好奇，什么都想去动一下，这是他们认识世界的一种方式。所以说孩子“不听话”，根本就是家长的误判，是家长管得太多了。 对孩子管的特别细特别严的家长，大都是在工作、生活等方面很用心的人，成功动机在他们的生命中始终比较强，他们的自我管理往往做的很好，在工作上或事业上属于那种放哪儿都会干好，都会取得一定成就的人。同样在孩子的教育上，他们成功心更切，也很自信，把对自己的管理，都拿去套用到孩子的身上。\n可是，他们基本上都失望了。 “不说”是件比“说”更难做到的事情。孩子的行为每天都在对你的心理形成挑战，这实在需要家长用足够的理智和耐心去消解这件事。 总之在教育孩子这件事情上，“不作为”才是最好的作为，“不管”就是做好的管。\n 图片来源于网络，如有侵权，请联系删除!','url':'http://k.sina.com.cn/article_6429310214_17f377d0600100cvoy.html'}

    client=AdIdentify()
    adlist=client.get_adlist(msg)
    print adlist
    for i in adlist:
        print i.get('ad_sen')

if __name__=='__main__':
    main()
