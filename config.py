import os
from datetime import datetime

token = None
if "TOKEN" in os.environ:
    token = os.environ["TOKEN"]
elif os.path.isfile("token"):
    with open("token") as f:
        token = f.read().strip()
else:
    raise AssertionError


class ImgApi:
    def __init__(self, url: str):
        self.url = url
        self.sep = "?" if "?" not in self.url else "&"

    def get(self) -> str:
        return f"{self.url}{self.sep}timestamp={datetime.now().timestamp()}"


api_url_list = [
    "https://api.66mz8.com/api/rand.acg.php?type=%E4%BA%8C%E6%AC%A1%E5%85%83",
    "https://api.66mz8.com/api/rand.acg.php?type=%E5%91%86%E8%90%8C%E9%85%B1",
    "https://api.66mz8.com/api/rand.acg.php?type=%E7%BE%8E%E5%A5%B3",
    "https://api.66mz8.com/api/rand.img.php?type=%E5%88%B6%E6%9C%8D",
    "https://api.66mz8.com/api/rand.img.php?type=%E6%80%A7%E6%84%9F",
    "https://api.66mz8.com/api/rand.img.php?type=%E7%BE%8E%E5%A5%B3",
    "https://api.66mz8.com/api/rand.tbimg.php",
    # 'https://pixiv.yoshino-s.workers.dev/random',
    "https://v1.alapi.cn/api/acg",
    "https://v1.alapi.cn/api/bing",
]

img_api_list = list(map(ImgApi, api_url_list))

cheater_list = [
    "我觉得你俩在一起特别合适，真的！因为你都不知道你有多优秀呢",
    "一个人的夜晚，好寂寞，好害怕，不过我要加油，要坚强！",
    "一直想努力跟她成为很好的闺蜜，可我不知道为什么她老是误会我。",
    "一起打排位你女朋友也要不高兴啊？那你别玩游戏了，好好陪她好了。",
    "不再见面也有不见面的好，你永远是我记忆中的样子",
    "不几道为笋么她们总是酱紫对偶，真是搞不清楚，她们好奇葩喔，你嗦呢，呕巴？",
    "不喜欢你了就是不喜欢你了",
    "不属于自己、又何必拼了命的去在乎。",
    "不开心了就来找我聊天，我可以陪你呀",
    "不开心难过的时候，和你说说就好了。",
    "不是说喜欢我吗，别再跟你那些朋友来往了。",
    "不要再来联系我，我不想你女朋友误会我们的关系。",
    "不许你这样说他，就算你俩是情侣，你也不能在我面前这样说他，他真的是好人。",
    "不许你这样说我干哥！虽然你俩是情侣，但是我不允许你在我面前这样。我哥真的是好人！",
    "不都是你主动的吗 我什么都没做啊",
    "今天去以前的学校，居然迷路了，发现自己真的是笨笨的呢！为什么不能像别人那样聪明。",
    "今天学习缝衣服，结果把五个手指都扎破了555，我发现自己真的好笨哦，要坚强，不要哭！",
    "今天我心情不好，你能来陪我吗？",
    "从来没有人这么理解过我。",
    "从没期待过，所以不存在失望",
    "他只是我的哥哥，你不要误会！我希望你们幸福的！",
    "他是我哥哥",
    "他最爱的人是我，你只是比我先一步认识他罢了。",
    "他的孩子你不配养",
    "你不懂我.......我以为你懂的......懂的人不需要讲，不懂的讲了也没用",
    "你不提分手我们就永远不会分手",
    "你不要怪她，是我让她多想了",
    "你不要总是觉得她控制了你的自由啦，其实她只是太喜欢你而已，我以前拍拖的时候哦，男朋友都说我太不管他呢，觉得感受不了爱。",
    "你不要生她的气了，我是女生我了解女生，你快去安慰她吧不要管我",
    "你不要这样，我们只是好哥们而已。",
    "你为我付出过什么 你为这份感情又付出过什么 好意思说问心无愧？ 不是你自己在那享受了？",
    "你为我付出那么多，都是自愿的，我没逼你",
    "你们因为我吵架，我很愧疚",
    "你做了那么多坏事，让我怎么相信你爱我，你还有什么要说的？",
    "你别误会，我和他真的没什么。",
    "你别跟姐姐闹别扭啦，她就是比较任性嘛，女孩子都有点小脾气的，要不我陪你散散心。",
    "你别这样说她了，她一定不想这样的。我帮你和她说说吧，你别生气了。你这样我也很难过",
    "你别闹 真没有 你说什么是什么",
    "你又跟别人联系，刚才跟你打电话的人是谁?",
    "你可不可以把我当妹妹啊",
    "你和她恋爱一定很辛苦吧",
    "你和我聊天姐姐会不会生气呀？",
    "你嘴边有东西，我帮你擦擦吧",
    "你回到你女朋友身边去吧，我可以的",
    "你太好了，我配不上你",
    "你女朋友不难看呀，怎么你给我们看的这张照片这么丑，明显没选好角度嘛。",
    "你女朋友好幸福，有你这么好的男朋友，要是我是她就好了。",
    "你女朋友好有福气，有你这么好的男友",
    "你女朋友是不是因为我不高兴了啊？",
    "你女朋友是不是误会了，都是我不好，让我去解释吧，好吗？",
    "你女朋友真会谈恋爱，把你治得服服帖帖的，真羡慕啊。",
    "你女朋友真凶，是我的话就不会这样",
    "你女朋友被你惯坏了，我好心疼你，如果是我一定不会那样的！",
    "你女朋友都被你宠坏了，你对她太好了，我肯定舍不得自己的男朋友这么辛苦。",
    "你女朋友长得不难看呀，怎么你给我们看的这张照片这么丑，明显没有选好角度嘛。",
    "你好像一直都没有搞清状况吧，我们不一直都是朋友而已吗？",
    "你快去哄你女朋友吧，她好像又生气了，我没事的",
    "你快回到你女朋友身边去吧，我不想伤害她。",
    "你把最宝贵的东西给了别人，你永远亏欠我",
    "你既然口口声声说爱我为什么不能相信我？",
    "你看不懂吗 话我不说第二遍",
    "你看你只跟你女友在一起玩，都忘掉我们这些哥们了。",
    "你真好，我怎么没遇见像你这么好的男朋友呢？我真是命苦，呜呜呜...。",
    "你知道吗你这个样子，除了我没人会要你。",
    "你知道吗？我一直对你有感觉，但是你有女朋友…我知道我不该打扰你，你就当不知道好了。好好跟她在一起，我永远在你身边默默陪着你。",
    "你要怪就怪我吧，我实在太爱他了",
    "你要记住，难过的时候一定要来找我哦",
    "你要跟我说对不起懂吗",
    "你要这么想我也没有什么办法",
    "你跟你女朋友感情怎么样？你上次不是跟我说你很烦她吗，到底怎么了？",
    "你这么丑  也就是我不嫌弃你",
    "你这么好的男人，她怎么不懂得珍惜呢。",
    "你这件衣服挺好看的，就是我穿不了啊，我的胸太大了。",
    "你那么好 我本来就不好 我当然做的就不好了",
    "先分开一段时间吧，都冷静冷静",
    "其实我挺喜欢你的，但是我们不合适",
    "其实我真的没有化妆~不会化妆~我是素颜哦~什么修照片？我不懂。。。我的照片都是我自己来~",
    "别黏着我，等我想要找你的时候就会找你的",
    "又是自己一个人过七夕，发现自己真的好笨，难怪不像别的女孩那样那么容易就有男友，不过我一个人也要加油哦！",
    "反正你们也是异地，你可不可以多陪陪我",
    "只要你们合好就好了，我没事。",
    "只要在你身边静静守候就可以了，别无所求。",
    "哇~你好好有肌肉，我可以捏捏吗？什么？不公平啊？哈哈。那你也捏捏我咯~嘶，好痛哦，轻点啦！",
    "哇你看那个女生化妆化得好好哦，照片也p的很好，我都不会化妆和ps，就只能每天素颜，也没有精美的照片上传。",
    "哇！为什么你裤头穿上会鼓鼓的 我可以捏捏么？ 不然你也捏我的？咱们不一样耶",
    "哇，你有腹肌哦，好厉害，可以给我摸摸吗？啊什么？不公平？那你可以摸摸我呀~哎呀哎呀 好痒哦~",
    "哎...真羡慕你女朋友，要是我也有个像你这样的男朋友就好了。",
    "哥哥，你怎么这么慢才回我消息，是不是，姐姐又生气啦。",
    "哥，别这样，我已经有男朋友了，虽然他对我并不好。",
    "哭的时候还拍照 特意吧眼泪浪出来下面还加一句 我很好很开心",
    "唉，你这样好的男人，她怎么就不懂得珍惜呢~？",
    "啊，好烦哦，又有人跟我表白了，我都不知道怎么拒绝他？",
    "喂？我好像喝多了，不知道打给谁，你能不能来接我",
    "因为我们是朋友，所以我们永远都不会分手对不对？",
    "多聊几个怎么了，我又不是打字慢",
    "她不是故意的，你别怪她",
    "她其实很好的，只是误会了我们而已，你不要对她这么凶呀？",
    "她平时玩得挺开的，开玩笑什么的也不介意。我觉得我就做不到和男生开那种玩笑，感觉自己好失败喏。",
    "她是不是生气了，你快去解释解释，我们没什么的，她误会了可不好。",
    "她真的很爱你，我没有破坏你们的意思",
    "她脾气是不是不太好啊",
    "好大的雨，我浑身都湿透了，如果你女朋友不在家的话，能借用一下你的卫生间洗个澡吗？",
    "如果我有男朋友了，你就不再理我了吗?",
    "如果是我，我一定能让你每天开心",
    "如果让你们之间不愉快了，那我退出吧",
    "对不起，我不是有意的，我不想你们因为我而吵架。",
    "对不起，我不知道这样她会生气呀？",
    "对不起，我已经有男朋友了，虽然他对我不怎么好",
    "对不起，我还爱他",
    "就算牵手了，我们还是朋友呀",
    "希望她比我更爱你，这就够了",
    "干嘛非要知道我全名 网名不好听嘛",
    "当初还不是看你家有钱，不然怎么会嫁给你",
    "得到时你在毁，失去后却在悔。",
    "怎么？生气了？那你来找我干嘛",
    "想念我的一个异性好友，那时候我总霸占他的床，我们总是搂在一起睡觉，脱的只剩胸衣和底裤，但是什么都不会发生，他尊重并且珍惜我，那是一种克制的友情。",
    "感情没有先来后到。",
    "感觉她蛮会吸引男孩子的，好羡慕哦。",
    "懂我的人，不必解释；不懂我的人，何必解释。",
    "我一直在努力想要和她成为很好的闺蜜，但是我不知道她为什么一直在针对我。",
    "我不想伤害任何人。",
    "我不想伤害任何人，我真的不知道事情怎么变成现在这样了。",
    "我不是故意绿你，我只是忘了说分手",
    "我不是渣，我是想给每个男孩子一个家",
    "我不知道她为什么这么爱针对我。",
    "我不知道怎么才能抓住男人的心，真的，看着其他人都能牢牢控制住男人，我真的不知道该怎么跟男孩子相处。",
    "我不能和你在一起，因为这样我们才永远都不会分手。",
    "我不要什么名分，你只要对我好就行了。",
    "我不要其他的，只要在你心里有我一个小小的角落我就满足了。",
    "我不跟你吵 随你便",
    "我也是为你好，只有我是真心对你",
    "我以前对其他女生不这样的 你应该感到幸福",
    "我们不要再见面了，我不想你女朋友误会我们的关系。",
    "我们只是朋友啊，你千万别多想",
    "我们总是在错误的时间，错误的地点，懵懵然就爱上那个人，然后，不得不用尽一生去遗忘",
    "我们能不能人生只若初见",
    "我会一直陪着你，不管你有多少女朋友，你要记住，难过的时候一定要来找我。",
    "我做这件事跟你想的出发点不一样啊",
    "我单身，我快乐，我想撩几个撩几个",
    "我只想默默喜欢你呀",
    "我只是帮他而已啦",
    "我只是绿了他，又不是绿了你",
    "我只要在你身边静静守候就可以了，别无所求。",
    "我只要远远看着你快乐就够了，希望她比我更爱你。",
    "我嘴边有东西，你能帮我擦擦吗",
    "我失恋了你陪陪我好吗？我喝醉了你送我回家好吗？我心情不好你陪我聊天 好吗？",
    "我好羡慕她会化妆哦，不像我这么笨，连擦粉底都不会。",
    "我对你的喜欢只能到退房哦",
    "我就这个脾气，受不了你就走",
    "我已经心怀愧疚了，你还要我怎样",
    "我已经忘了如何去心动，去爱。",
    "我想自由一点",
    "我懂你的，你也别怪她，她只是现在气头上顾及不了你。有什么不开心可以跟我说，谁叫我们是好知己呢。天气开始转凉了，照顾好自己呀。",
    "我是个有原则的人，我的原则就是看心情",
    "我有喜欢的人了，可我好想跟你做朋友，因为我觉得我们很像，对不对。",
    "我没说过我是好人吧",
    "我爱你，但她更爱你，我成全你们",
    "我爱你，可是你总让我失望，我感受不到你的爱",
    "我生孩子那么疼，你还在乎是不是你的",
    "我真的不是故意的，她一定是误会了",
    "我真的不知道该怎么跟男孩子相处",
    "我真的只想和你做朋友",
    "我真的只是当他是哥哥而已。",
    "我真的只是把他当哥哥",
    "我真的好喜欢她这样随性的人呀，家里乱乱的，酒量好，可以随意的说脏话，我就不行，我说 不出口。",
    "我真的好心疼你，但是现在我没有那个资格",
    "我真的很讨厌别人不信任我",
    "我真的是把你的男朋友当做哥哥，你不要误会了好么？虽然他很好，下雨了会帮我打伞，但是你不要误会我们",
    "我知道你有女朋友，我也不想你为难，看完记得八聊天记录删了。",
    "我等你给我介绍和你一样的男朋友",
    "我被骂没什么，但我不想看到你不开心",
    "我要是你女朋友肯定舍不得你这么累的。我要是你女朋友肯定会理解你的。我要是你女朋友绝对不是这么小心眼的。",
    "我觉得你是个想太多的人。",
    "我认为爱不是去改变或者拯救一个人，是找到那个早已合适你的人。",
    "我跟他不是你想的那样的关系",
    "我跟他只是吃了饭看了电影逛了街而已，真的没有做什么，因为你们最近感情不好，所以我才像说出来帮你陪陪他……",
    "我跟他在一起就为了气你",
    "我还是喜欢你的",
    "我逼你了吗？不是你自己愿意的？",
    "我遇到过很多漂亮的女人，但我选了你",
    "我难道没有自己的事吗？你以为和你一样那么闲？",
    "昨天给你发短信的时候还小小的期待过你会马上回我电话呢，那个时候你在陪女朋友吧？有你这样的男生陪着，她真的好幸福哦。",
    "是你要分手的不是我说的",
    "是你错了，别的女孩子就不会这样",
    "是我不对，我以为她不会介意的",
    "有两个男生在追我，我不都试一下，怎么知道哪个合适",
    "有你这样的男生陪着她，她真幸福",
    "没想到她会介意的，我去给她道歉吧",
    "然后呢？所以呢？你还想怎样？",
    "爱我，你就吞下去",
    "爱笑的姑娘运气都不会太差",
    "现在有空吗？我心情好难过，能陪我聊聊天吗？",
    "用心甘情愿的态度，过随遇而安的生活。",
    "真可惜，我要是早认识你就好了",
    "真的不知道事情怎么会变成这样。",
    "真的好羡慕你女朋友那么会化妆，不像我，出门涂个防晒都不会。",
    "真的对不起，我只是把你当做好朋友，我不知道原来你喜欢我。",
    "老公你原谅我吧，我会报答你的",
    "虽然她这么作，但是你一直很有耐心啊",
    "虽然我以前很渣 但是自从遇见你我现在想改变我的生活",
    "虽然陪在你身边的都不会是我，但你不开心的时候我都会一样难过。",
    "要不要我去帮你跟她解释一下？",
    "让你女友多想了，我们还是不要说话了",
    "记得把我跟你的聊天记录删了，别让姐姐看到了误会。",
    "说实话，你女朋友是有点小气",
    "走一个忘一个，永远还有下一个",
    "跟喜欢我的男生说 也只有她能让你难过 我再怎么气你你也只是一笑而过罢了 我曾经的闺蜜 哈哈",
    "跟我一样的女孩那么多，可我要的是惟一。",
    "这么晚我是不是不该打扰你，对不起",
    "这么给你说吧我真的挺爱你的 相不相信你看着办吧",
    "这件衣服挺好看的，就是我穿不了啊，我的胸太大了。",
    "这是我最后一次叫你哥哥了，我们还是不要再联系了好吗？我不想让嫂子不开心。",
    "这话可是你说的啊 我可没那意思",
    "那天我喝多了，所以才睡在他家",
    "都是你一直逼我 不是一直都是你说了算嘛",
]
