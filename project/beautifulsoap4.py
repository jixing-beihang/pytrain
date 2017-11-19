html = '''
"D:\Software\Python 3.6.3\python.exe" D:/Software/PyCharm/Workspace/project/re_application.py
<!DOCTYPE HTML>
<html lang="zh-cmn-Hans" class="">
<head>
<meta charset="UTF-8">
<meta name="description" content="提供图书、电影、音乐唱片的推荐、评论和价格比较，以及城市独特的文化生活。">
<meta name="keywords" content="豆瓣,广播,登陆豆瓣">
<meta property="qc:admins" content="2554215131764752166375" />
<meta property="wb:webmaster" content="375d4a17a4fa24c2" />
<meta name="mobile-agent" content="format=html5; url=https://m.douban.com">
<title>豆瓣</title>
<script>
function set_cookie(t,e,o,n){var i,a,r=new Date;r.setTime(r.getTime()+24*(e||30)*60*60*1e3),i="; expires="+r.toGMTString();for(a in t)document.cookie=a+"="+t[a]+i+"; domain="+(o||"douban.com")+"; path="+(n||"/")}function get_cookie(t){var e,o,n=t+"=",i=document.cookie.split(";");for(e=0;e<i.length;e++){for(o=i[e];" "==o.charAt(0);)o=o.substring(1,o.length);if(0===o.indexOf(n))return o.substring(n.length,o.length).replace(/\"/g,"")}return null}window.Douban=window.Douban||{};var Do=function(){Do.actions.push([].slice.call(arguments))};Do.ready=function(){Do.actions.push([].slice.call(arguments))},Do.add=Do.define=function(t,e){Do.mods[t]=e},Do.global=function(){Do.global.mods=Array.prototype.concat(Do.global.mods,[].slice.call(arguments))},Do.global.mods=[],Do.mods={},Do.actions=[],Douban.init_show_login=function(t){Do("dialog",function(){var t="/j/misc/login_form";dui.Dialog({title:"登录",url:t,width:/device-mobile/i.test(document.documentElement.className)?.9*document.documentElement.offsetWidth:350,cache:!0,callback:function(t,e){e.node.addClass("dialog-login"),e.node.find("h2").css("display","none"),e.node.find(".hd h3").replaceWith(e.node.find(".bd h3")),e.node.find("form").css({border:"none",width:"auto",padding:"0"}),e.update()}}).open()})},Do(function(){function t(t,e){var o=["ref="+encodeURIComponent(location.pathname)];for(var n in e)e.hasOwnProperty(n)&&o.push(n+"="+e[n]);window._SPLITTEST&&o.push("splittest="+window._SPLITTEST),localStorage.setItem("report",(localStorage.getItem("report")||"")+"_moreurl_separator_"+o.join("&"))}!function(){"localStorage"in window||(window.localStorage=function(){var t=document;if(!t.documentElement.addBehavior)throw"don't support localstorage or userdata.";var e="_localstorage_ie",o=t.createElement("input");o.type="hidden";var n=function(n){return function(){t.body.appendChild(o),o.addBehavior("#default#userData");var i=new Date;i.setDate(i.getDate()+365),o.expires=i.toUTCString(),o.load(e);var a=n.apply(o,arguments);return t.body.removeChild(o),a}};return{getItem:n(function(t){return this.getAttribute(t)}),setItem:n(function(t,o){this.setAttribute(t,o),this.save(e)}),removeItem:n(function(t){this.removeAttribute(t),this.save(e)}),clear:n(function(){for(var t,o=this.XMLDocument.documentElement.attributes,n=0;t=o[n];n++)this.removeAttribute(t.name);this.save(e)})}}())}(),$(window).one("load",function(){var t=localStorage.getItem("report");if(t){t=t.split("_moreurl_separator_");var e=function(o){return""==o?void e(t.shift()):void $.get("undefined"==typeof _MOREURL_REQ?"/stat.html?"+o:_MOREURL_REQ+"?"+o,function(){return t.length?(e(t.shift()),void localStorage.setItem("report",t.join("_moreurl_separator_"))):void localStorage.removeItem("report")})};e(t.shift())}}),window.moreurl=t,$(document).click(function(e){var o=e.target,n=$(o).data("moreurl-dict");n&&t(o,n)}),$.ajax_withck=function(t){return"POST"==t.type&&(t.data=$.extend(t.data||{},{ck:get_cookie("ck")})),$.ajax(t)},$.postJSON_withck=function(t,e,o){return $.post_withck(t,e,o,"json")},$.post_withck=function(t,e,o,n){return $.isFunction(e)&&(n=o,o=e,e={}),$.ajax({type:"POST",url:t,data:$.extend(e,{ck:get_cookie("ck")}),success:o,dataType:n||"text"})},$("html").click(function(t){var e=$(t.target),o=e.attr("class");o&&$(o.match(/a_(\w+)/gi)).each($.proxy(function(e,o){var n=Douban[o.replace(/^a_/,"init_")];"function"==typeof n&&(t.preventDefault(),n.call(this,t))},e[0]))})});

Do.add('dialog', {path: 'https://img3.doubanio.com/f/shire/4ea3216519a6183c7bcd4f7d1a6d4fd57ce1a244/js/ui/dialog.js', type: 'js', requires: ['https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css']});
Do.global('https://img3.doubanio.com/f/sns/b5793c2d7c298173d57ecf7d96708b5615336def/js/sns/fp/base.js', 'dialog');
</script>
<link rel="stylesheet" href="https://img3.doubanio.com/f/shire/8b9fa55c839b74f72d2279a4f6839a2c8a1a9553/css/core/_init_.css">
<link rel="stylesheet" href="https://img3.doubanio.com/f/sns/024dd07167e74fe8d2ac2faaf2725333e6f7561b/css/sns/anonymous_home.css">
<style type="text/css">
.rec_topics_name{
    display: inline-block;
    margin-bottom: 6px;
    font-size: 14px;
    line-height: 1;
    color: #3377aa;
}
.rec_topics_subtitle{
    display: block;
    margin-bottom: 15px;
    font-size: 13px;
    line-height: 1;
    color: #aaaaaa;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.rec_topics_label{
    transform: translateY(-0.5px);
    display: inline-block;
    font-size: 13px;
    margin-left: 2px;
}
.rec_topics{
    line-height: 1;
    margin-bottom: 15px;
}
.rec_topics:last-child{
    margin-bottom: 0;
}
.rec_topics_label_ad{
    color: #c9c9c9;
    -moz-transform: scale(0.91);
    -webkit-transform: scale(0.91);
    transform: scale(0.91);
}

html[class*=ua-ff] .rec_topics_subtitle{
    line-height: 14px;
}

</style>
</head>

<body>
<div id="anony-nav">
    <div class="anony-nav-links">
    <ul>
    <li> <a target="_blank" class="lnk-book" href="https://book.douban.com">豆瓣读书</a></li>
    <li> <a target="_blank" class="lnk-movie" href="https://movie.douban.com">豆瓣电影</a></li>
    <li> <a target="_blank" class="lnk-music" href="https://music.douban.com">豆瓣音乐</a></li>
    <li> <a target="_blank" class="lnk-group" href="https://www.douban.com/group/">豆瓣小组</a></li>
    <li> <a target="_blank" class="lnk-events" href="https://www.douban.com/location/">豆瓣同城</a></li>
    <li> <a target="_blank" class="lnk-fm" href="https://douban.fm">豆瓣FM</a></li>
    <li> <a target="_blank" class="lnk-shijian" href="https://www.douban.com/time/?dt_time_source=douban-web_anonymous_index_top_nav">豆瓣时间</a></li>
    <li> <a target="_blank" class="lnk-market" href="https://market.douban.com?utm_campaign=anonymous_top_nav&utm_source=douban&utm_medium=pc_web">豆瓣市集</a></li>
    </ul>
    </div>

    <h1><a href="https://www.douban.com">豆瓣</a></h1>

    <div class="anony-srh">
    <form action="https://www.douban.com/search" method="get">
      <span class="inp"><input type="text" maxlength="60" size="12" placeholder="书籍、电影、音乐、小组、小站、成员" name="q" autocomplete="off"></span>
    <span class="bn"><input type="submit" value="搜索"></span>
    </form>
    </div>
  </div>
  
  <div class="albums">
    <ul>
      <li>
      <div class="pic">
          <a href="https://www.douban.com/photos/album/1654330413/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/photo/albumcover/public/p2503869405.jpg" alt="" /></a>
      </div>
      <a href="https://www.douban.com/photos/album/1654330413/">布达佩斯</a>
      <span class="num">21张照片</span>
      <li>
      <div class="pic">
          <a href="https://www.douban.com/photos/album/1653314391/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img3.doubanio.com/view/photo/albumcover/public/p2501467160.jpg" alt="" /></a>
      </div>
      <a href="https://www.douban.com/photos/album/1653314391/">在坦桑尼亚度假</a>
      <span class="num">71张照片</span>
      <li>
      <div class="pic">
          <a href="https://www.douban.com/photos/album/155204867/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/photo/albumcover/public/p2236390609.jpg" alt="" /></a>
      </div>
      <a href="https://www.douban.com/photos/album/155204867/">啊哈建筑 | 当建筑酱邂逅COSPLAY</a>
      <span class="num">12张照片</span>
      <li>
      <div class="pic">
          <a href="https://www.douban.com/photos/album/1654090498/"><img src="https://img3.doubanio.com/f/shire/a1fdee122b95748d81cee426d717c05b5174fe96/pics/blank.gif" data-origin="https://img1.doubanio.com/view/photo/albumcover/public/p2503271837.jpg" alt="" /></a>
      </div>
      <a href="https://www.douban.com/photos/album/1654090498/">「你未曾注意过的日本下町」</a>
      <span class="num">39张照片</span>
    </ul>
  </div>
  <div class="notes">
    <ul>
      <li class="first">
      <div class="title">
          <a href="https://www.douban.com/note/644472898/">二大爷死了</a>
      </div>
      <div class="author">
        青崖白鹿的日记
      </div>
      <p>我二大爷前两年就死了，我妈打电话告诉我，说他死在了村西头的小后屋里。被发现时...</p>
      </li>

      <li><a href="https://www.douban.com/note/644468411/">办公室一幕</a></li>
      <li><a href="https://www.douban.com/note/641995493/">酿酒师</a></li>
      <li><a href="https://www.douban.com/note/644718748/">唇膏大赏｜我不能没有的唇膏们 PART I</a></li>
      <li><a href="https://www.douban.com/note/644602148/">一次学会关东煮和寿喜烧！</a></li>
      <li><a href="https://www.douban.com/note/634640585/">头条新闻</a></li>
      <li><a href="https://www.douban.com/note/644551118/">妖风河往事之芦传捷</a></li>
      <li><a href="https://www.douban.com/note/641400797/">我一生中的两次葬礼</a></li>
      <li><a href="https://www.douban.com/note/644423079/">“小景” 和 “宏图”</a></li>
      <li><a href="https://www.douban.com/note/644641979/">作为医生，我在ICU病房中经历的第一场死亡 | 三明治</a></li>
    </ul>
  </div>
</div>
</div>
  </div>
  

</div>'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')

# HTML 标签选择器
# print(soup.prettify())
# print(soup.title.string)
# print(soup.body)
# print(soup.p)

# find_all() name=''
# print(soup.find_all('ul'))
# print(soup.find_all('ul')[0])
# for ul in soup.find_all('ul'):
#     print(ul.find_all('li'))

# attrs={}
# print(soup.find_all(attrs={'class':'title'}))
# print(soup.find_all(id="anony-nav"))
# print(soup.find_all(attrs={'class':'author'}))
# print(soup.find_all(class_='author'))

# text=''
# print(soup.find_all(text='在坦桑尼亚度假'))

# CSS样式选择器 select  .代表类，#代表id，ul、li、a、p标签
# print(soup.select('.albums .pic'))
# print(soup.select('ul li'))
# print(soup.select('#anony-nav .anony-srh'))

# 嵌套查找，获取属性[]
# for ul in soup.select('.albums .pic'):
#     print(type(ul))
#     for a in ul.select('a'):
#         print(a['href'])
#         print(a.attrs['href'])

# 获得内容 get_text
for li in soup.select('li'):
    print(li.text)
    print(li.get_text)