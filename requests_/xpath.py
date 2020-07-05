from scrapy import Selector

html="""

<html><head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <meta http-equiv="Content-Type" content="text/html; charset=gbk">
    <title>【上海,python招聘，求职】-前程无忧</title>
    <meta name="description" content="前程无忧为您提供最新最全的上海,python招聘，求职信息。网聚全国各城市的人才信息，找好工作，找好员工，上前程无忧。">
    <meta name="keywords" content="找工作,求职,人才,招聘">
    <meta name="mobile-agent" content="format=html5; url=https://m.51job.com/search/joblist.php?jobarea=020000&amp;keyword=python&amp;partner=webmeta">
    <meta name="mobile-agent" content="format=xhtml; url=https://m.51job.com/search/joblist.php?jobarea=020000&amp;keyword=python&amp;partner=webmeta">
    <meta name="robots" content="all">
    <meta http-equiv="Expires" content="0">
    <meta http-equiv="Cache-Control" content="no-cache">
    <meta http-equiv="Pragma" content="no-cache">
    <link rel="dns-prefetch" href="//js.51jobcdn.com">
    <link rel="dns-prefetch" href="//img01.51jobcdn.com">
    <link rel="dns-prefetch" href="//img02.51jobcdn.com">
    <link rel="dns-prefetch" href="//img03.51jobcdn.com">
    <link rel="dns-prefetch" href="//img04.51jobcdn.com">
    <link rel="dns-prefetch" href="//img05.51jobcdn.com">
    <link rel="dns-prefetch" href="//img06.51jobcdn.com">
    <script language="javascript" src="//js.51jobcdn.com/in/js/2016/jquery.js?20180319"></script>
    <script language="javascript">
    var _tkd = _tkd || []; //点击量统计用
    var lang = [];
    var supporthttps = 1; //浏览器是否支持https
    var currenthttps = (window.location.protocol === 'https:') ? '1' : '0'; //当前是否为https
    var systemtime = 1593948210031;
    var d_system_client_time = systemtime - new Date().getTime();
    var trackConfig = {
        'guid': 'd4c820d7e7291331733ed54e2248c47b',
        'ip': '113.100.36.170',
        'accountid': '',
        'refpage': '',
        'refdomain': '',
        'domain': 'search.51job.com',
        'pageName': 'index.php',
        'partner': '',
        'islanding': '0',
    };
    window.cfg = {
        lang:'c',
        domain : {
            my : 'http://my.51job.com',
            login : 'https://login.51job.com',
            search : 'https://search.51job.com',
            www : '//www.51job.com',
            jobs : 'https://jobs.51job.com',
            jianli : 'https://jianli.51job.com',
            company : '//company.51job.com',
            i : '//i.51job.com',
            jc : '//jc.51job.com',
            map : 'https://map.51job.com',
            m : 'https://m.51job.com',
            cdn : '//js.51jobcdn.com',
            help : 'https://help.51job.com',
            img : '//img06.51jobcdn.com',
            dj : '//dj.51job.com',
            mdj : '//mdj.51job.com',
            mq : '//mq.51job.com',
            mmq : '//mmq.51job.com',
            kbc : 'https://kbc.51job.com',
            mtr : 'https://medu.51job.com',
            tr : 'https://edu.51job.com',
        }
    };

window.cfg.lang = 'c';
window.cfg.fullLang = 'Chinese';
window.cfg.url = {
root : 'https://search.51job.com',
image : '//img04.51jobcdn.com/im/2009',
image_search : '//img01.51jobcdn.com/im/2009/search',
i : '//i.51job.com'
}
window.cfg.fileName = 'index.php';
window.cfg.root = 'https://search.51job.com';
window.cfg.root_userset_ajax = '//i.51job.com/userset/ajax';
window.cfg.isSearchDomain = '1';
window.cfg.langs = {
sqzwml : 'applyjob',
qzzwqdg : '请在要选择的职位前打勾!',
myml : 'my',
ts_qxjzw : '请选择职位',
queren : '确认',
guanbi : '关闭',
nzdnxj : '您最多能选择',
xiang : '项',
xzdq : '选择地区',
xj_xg : '选择/修改',
zycs : '主要城市',
sysf : '所有省份',
tspd : '特殊频道',
buxian : '不限',
qingxj : '请选择',
yixuan : '已选',
znlb : '职能类别',
hylb : '行业类别',
gzdd : '工作地点',
quanbu : '全部',
zhineng : '职能',
hangye : '行业',
didian : '地点',
qsrgjz : '请输入关键字',
srpcgjz : '输入排除关键字'
}
window.cfg.stype = '1';
window.cfg.isJobview = '1';
</script>
<script type="text/javascript" src="//js.51jobcdn.com/in/js/2016/pointtrack.js?20180605"></script>

    <script language="javascript" src="//js.51jobcdn.com/in/js/2016/login/jquery.placeholder.min.js"></script>
    <link href="//js.51jobcdn.com/in/resource/css/2020/search/common.848e2ce1.css" rel="stylesheet">
<link href="//js.51jobcdn.com/in/resource/css/2020/search/searchResult.4bd31223.css" rel="stylesheet">
<script type="text/javascript" src="https://js.51jobcdn.com/in/js/2016/trace/trackData.js?20180206"></script></head>
<body>
<div class="header">
    <!-- bar start -->
    <div class="bar">
        <div class="in">
            <div class="language">
                <ul id="languagelist">
                    <li class="tle"><span class="list">简</span></li><li><a href="http://big5.51job.com/gate/big5/www.51job.com/" rel="external nofollow">繁</a></li><li class="last"><a href="//www.51job.com/default-e.php" rel="external nofollow">EN</a></li>                    <script language="javascript">
                        if(location.hostname == "big5.51job.com")
                        {
                            $('#languagelist li span').html("繁");
                            $('#languagelist li:nth-child(2) a').html("简");
                            $('#languagelist li:nth-child(2) a').attr('href','javascript:void(0)');
                            $('#languagelist li:nth-child(2) a').click(function(){location.href=window.cfg.domain.www});
                            $('#languagelist li:nth-child(3) a').attr('href','javascript:void(0)');
                            $('#languagelist li:nth-child(3) a').click(function(){location.href=window.cfg.domain.www+"/default-e.php"});
                        }
                    </script>
                </ul>
            </div>
            <span class="l">&nbsp;</span>
            <div class="app">
                <ul>
                    <li><em class="e_icon"></em><a href="http://app.51job.com/index.html">APP下载</a></li>
                    <li>
                        <img width="80" height="80" src="//img02.51jobcdn.com/im/2016/code/new_app.png" alt="app download">
                        <p><a href="http://app.51job.com/index.html">APP下载</a></p>
                    </li>
                </ul>
            </div>
            <div class="uer">
                                    <p class="op">
                        <a href="https://login.51job.com/login.php?lang=c&amp;url=http%3A%2F%2Fsearch.51job.com%2Flist%2F020000%2C000000%2C0000%2C00%2C9%2C99%2Cpython%2C2%2C1.html%3Flang%3Dc%26stype%3D%26postchannel%3D0000%26workyear%3D99%26cotype%3D99%26degreefrom%3D99%26jobterm%3D99%26companysize%3D99%26providesalary%3D99%26lonlat%3D0%252C0%26radius%3D-1%26ord_field%3D0%26confirmdate%3D9%26fromType%3D%26dibiaoid%3D0%26address%3D%26line%3D%26specialarea%3D00%26from%3D%26welfare%3D%2520%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%2520%25E7%2589%2588%25E6%259D%2583%25E5%25A3%25B0%25E6%2598%258E%25EF%25BC%259A%25E6%259C%25AC%25E6%2596%2587%25E4%25B8%25BACSDN%25E5%258D%259A%25E4%25B8%25BB%25E3%2580%258C%25E5%25BC%25A0%25E6%25B6%25A6%25E7%25BA%25A2%25E3%2580%258D%25E7%259A%2584%25E5%258E%259F%25E5%2588%259B%25E6%2596%2587%25E7%25AB%25A0%25EF%25BC%258C%25E9%2581%25B5%25E5%25BE%25AACC%25204.0%2520BY-SA%25E7%2589%2588%25E6%259D%2583%25E5%258D%258F%25E8%25AE%25AE%25EF%25BC%258C%25E8%25BD%25AC%25E8%25BD%25BD%25E8%25AF%25B7%25E9%2599%2584%25E4%25B8%258A%25E5%258E%259F%25E6%2596%2587%25E5%2587%25BA%25E5%25A4%2584%25E9%2593%25BE%25E6%258E%25A5%25E5%258F%258A%25E6%259C%25AC%25E5%25A3%25B0%25E6%2598%258E%25E3%2580%2582%2520%25E5%258E%259F%25E6%2596%2587%25E9%2593%25BE%25E6%258E%25A5%25EF%25BC%259Ahttps%3A%2F%2Fblog.csdn.net%2FZhangrunhong%2Farticle%2Fdetails%2F103054281" rel="external nofollow">登录</a> / <a href="https://login.51job.com/register.php?lang=c&amp;url=http%3A%2F%2Fsearch.51job.com%2Flist%2F020000%2C000000%2C0000%2C00%2C9%2C99%2Cpython%2C2%2C1.html%3Flang%3Dc%26stype%3D%26postchannel%3D0000%26workyear%3D99%26cotype%3D99%26degreefrom%3D99%26jobterm%3D99%26companysize%3D99%26providesalary%3D99%26lonlat%3D0%252C0%26radius%3D-1%26ord_field%3D0%26confirmdate%3D9%26fromType%3D%26dibiaoid%3D0%26address%3D%26line%3D%26specialarea%3D00%26from%3D%26welfare%3D%2520%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%25E2%2580%2594%2520%25E7%2589%2588%25E6%259D%2583%25E5%25A3%25B0%25E6%2598%258E%25EF%25BC%259A%25E6%259C%25AC%25E6%2596%2587%25E4%25B8%25BACSDN%25E5%258D%259A%25E4%25B8%25BB%25E3%2580%258C%25E5%25BC%25A0%25E6%25B6%25A6%25E7%25BA%25A2%25E3%2580%258D%25E7%259A%2584%25E5%258E%259F%25E5%2588%259B%25E6%2596%2587%25E7%25AB%25A0%25EF%25BC%258C%25E9%2581%25B5%25E5%25BE%25AACC%25204.0%2520BY-SA%25E7%2589%2588%25E6%259D%2583%25E5%258D%258F%25E8%25AE%25AE%25EF%25BC%258C%25E8%25BD%25AC%25E8%25BD%25BD%25E8%25AF%25B7%25E9%2599%2584%25E4%25B8%258A%25E5%258E%259F%25E6%2596%2587%25E5%2587%25BA%25E5%25A4%2584%25E9%2593%25BE%25E6%258E%25A5%25E5%258F%258A%25E6%259C%25AC%25E5%25A3%25B0%25E6%2598%258E%25E3%2580%2582%2520%25E5%258E%259F%25E6%2596%2587%25E9%2593%25BE%25E6%258E%25A5%25EF%25BC%259Ahttps%3A%2F%2Fblog.csdn.net%2FZhangrunhong%2Farticle%2Fdetails%2F103054281" rel="external nofollow">注册</a>                    </p>
                            </div>
			<p class="rlk">
                <a href="//baike.51job.com" target="_blank">职场百科</a>
                <span class="lb">&nbsp;</span>
                <a href="//wenku.51job.com" target="_blank">职场文库</a>
                <span class="lb">&nbsp;</span>
                <a href="https://jobs.51job.com" target="_blank">招聘信息</a>                <span class="lb">&nbsp;</span>
                <a href="https://ehire.51job.com" target="_blank">企业服务</a>            </p>
        </div>
    </div>
    <!-- top end -->
    <!-- 英文版为body添加class -->
    <script>
            </script>
    <!-- nag start -->
    <div class="pop-city" style="display:none;position: absolute; z-index: 1000;" id="area_channel_layer">
    <div class="tle">
        地区选择        <em class="close" onclick="jvascript:$('#area_channel_layer,#area_channel_layer_backdrop').hide();"></em>
    </div>
    <div class="pcon">
        <div class="ht">
            <label>热门城市</label><a href="//www.51job.com/beijing/">北京</a><a href="//www.51job.com/shanghai/">上海</a><a href="//www.51job.com/guangzhou/">广州</a><a href="//www.51job.com/shenzhen/">深圳</a><a href="//www.51job.com/wuhan/">武汉</a><a href="//www.51job.com/xian/">西安</a><a href="//www.51job.com/hangzhou/">杭州</a><a href="//www.51job.com/nanjing/">南京</a><a href="//www.51job.com/chengdu/">成都</a><a href="//www.51job.com/chongqing/">重庆</a>        </div>
        <div class="cbox">
            <ul id="area_channel_layer_list">
                <li class="on" onclick="areaChannelChangeTab('abc', this)">A B C</li>
                <li onclick="areaChannelChangeTab('def', this)">D E F</li>
                <li onclick="areaChannelChangeTab('gh', this)">G H</li>
                <li onclick="areaChannelChangeTab('jkl', this)">J K L</li>
                <li onclick="areaChannelChangeTab('mnp', this)">M N P</li>
                <li onclick="areaChannelChangeTab('qrs', this)">Q R S</li>
                <li onclick="areaChannelChangeTab('twx', this)">T W X</li>
                <li onclick="areaChannelChangeTab('yz', this)">Y Z</li>
            </ul>
            <div class="clst" id="area_channel_layer_all">
                    <div class="e" name="area_channel_div_abc">
        <span><a href="//www.51job.com/anshan/">鞍山</a></span>
        <span><a href="//www.51job.com/anqing/">安庆</a></span>
        <span><a href="//www.51job.com/anyang/">安阳</a></span>
        <span><a href="//www.51job.com/beijing/">北京</a></span>
        <span><a href="//www.51job.com/baotou/">包头</a></span>
        <span><a href="//www.51job.com/baoding/">保定</a></span>
        <span><a href="//www.51job.com/bengbu/">蚌埠</a></span>
        <span><a href="//www.51job.com/baoji/">宝鸡</a></span>
        <span><a href="//www.51job.com/binzhou/">滨州</a></span>
        <span><a href="//www.51job.com/changchun/">长春</a></span>
        <span><a href="//www.51job.com/changsha/">长沙</a></span>
        <span><a href="//www.51job.com/chengdu/">成都</a></span>
        <span><a href="//www.51job.com/chongqing/">重庆</a></span>
        <span><a href="//www.51job.com/changzhou/">常州</a></span>
        <span><a href="//www.51job.com/changde/">常德</a></span>
        <span><a href="//www.51job.com/changshu/">常熟</a></span>
        <span><a href="//www.51job.com/cangzhou/">沧州</a></span>
        <span><a href="//www.51job.com/chaozhou/">潮州</a></span>
        <span><a href="//www.51job.com/chenzhou/">郴州</a></span>
        <span><a href="//www.51job.com/chifeng/">赤峰</a></span>
        <span><a href="//www.51job.com/chuzhou/">滁州</a></span>
        <span><a href="//www.51job.com/changzhi/">长治</a></span>
    </div>
    <div class="e" name="area_channel_div_def" style="display:none">
        <span><a href="//www.51job.com/dalian/">大连</a></span>
        <span><a href="//www.51job.com/dongguan/">东莞</a></span>
        <span><a href="//www.51job.com/dandong/">丹东</a></span>
        <span><a href="//www.51job.com/daqing/">大庆</a></span>
        <span><a href="//www.51job.com/dazhou/">达州</a></span>
        <span><a href="//www.51job.com/datong/">大同</a></span>
        <span><a href="//www.51job.com/deyang/">德阳</a></span>
        <span><a href="//www.51job.com/dezhou/">德州</a></span>
        <span><a href="//www.51job.com/dongying/">东营</a></span>
        <span><a href="//www.51job.com/errduosi/">鄂尔多斯</a></span>
        <span><a href="//www.51job.com/ezhou/">鄂州</a></span>
        <span><a href="//www.51job.com/fuzhou/">福州</a></span>
        <span><a href="//www.51job.com/foshan/">佛山</a></span>
        <span><a href="//www.51job.com/fushun/">抚顺</a></span>
        <span><a href="//www.51job.com/fuzhoue/">抚州</a></span>
        <span><a href="//www.51job.com/fuyang/">阜阳</a></span>
    </div>
    <div class="e" name="area_channel_div_gh" style="display:none">
        <span><a href="//www.51job.com/guangzhou/">广州</a></span>
        <span><a href="//www.51job.com/guiyang/">贵阳</a></span>
        <span><a href="//www.51job.com/ganzhou/">赣州</a></span>
        <span><a href="//www.51job.com/guangan/">广安</a></span>
        <span><a href="//www.51job.com/guangyuan/">广元</a></span>
        <span><a href="//www.51job.com/guigang/">贵港</a></span>
        <span><a href="//www.51job.com/guilin/">桂林</a></span>
        <span><a href="//www.51job.com/harbin/">哈尔滨</a></span>
        <span><a href="//www.51job.com/hangzhou/">杭州</a></span>
        <span><a href="//www.51job.com/hefei/">合肥</a></span>
        <span><a href="//www.51job.com/haikou/">海口</a></span>
        <span><a href="//www.51job.com/huhhot/">呼和浩特</a></span>
        <span><a href="//www.51job.com/huizhou/">惠州</a></span>
        <span><a href="//www.51job.com/hengyang/">衡阳</a></span>
        <span><a href="//www.51job.com/huaian/">淮安</a></span>
        <span><a href="//www.51job.com/huzhou/">湖州</a></span>
        <span><a href="//www.51job.com/handan/">邯郸</a></span>
        <span><a href="//www.51job.com/hanzhong/">汉中</a></span>
        <span><a href="//www.51job.com/heyuan/">河源</a></span>
        <span><a href="//www.51job.com/heze/">菏泽</a></span>
        <span><a href="//www.51job.com/hengshui/">衡水</a></span>
        <span><a href="//www.51job.com/huaihua/">怀化</a></span>
        <span><a href="//www.51job.com/huaibei/">淮北</a></span>
        <span><a href="//www.51job.com/huainan/">淮南</a></span>
        <span><a href="//www.51job.com/huanggang/">黄冈</a></span>
        <span><a href="//www.51job.com/huangshi/">黄石</a></span>
    </div>
    <div class="e" name="area_channel_div_jkl" style="display:none">
        <span><a href="//www.51job.com/jinan/">济南</a></span>
        <span><a href="//www.51job.com/jiaxing/">嘉兴</a></span>
        <span><a href="//www.51job.com/jinhua/">金华</a></span>
        <span><a href="//www.51job.com/jilin/">吉林</a></span>
        <span><a href="//www.51job.com/jiangmen/">江门</a></span>
        <span><a href="//www.51job.com/jingzhou/">荆州</a></span>
        <span><a href="//www.51job.com/jining/">济宁</a></span>
        <span><a href="//www.51job.com/jiujiang/">九江</a></span>
        <span><a href="//www.51job.com/jian/">吉安</a></span>
        <span><a href="//www.51job.com/jiaozuo/">焦作</a></span>
        <span><a href="//www.51job.com/jieyang/">揭阳</a></span>
        <span><a href="//www.51job.com/jinzhou/">锦州</a></span>
        <span><a href="//www.51job.com/jinzhong/">晋中</a></span>
        <span><a href="//www.51job.com/jingmen/">荆门</a></span>
        <span><a href="//www.51job.com/kunming/">昆明</a></span>
        <span><a href="//www.51job.com/kunshan/">昆山</a></span>
        <span><a href="//www.51job.com/kaifeng/">开封</a></span>
        <span><a href="//www.51job.com/lanzhou/">兰州</a></span>
        <span><a href="//www.51job.com/langfang/">廊坊</a></span>
        <span><a href="//www.51job.com/linyi/">临沂</a></span>
        <span><a href="//www.51job.com/luoyang/">洛阳</a></span>
        <span><a href="//www.51job.com/lianyungang/">连云港</a></span>
        <span><a href="//www.51job.com/liuzhou/">柳州</a></span>
        <span><a href="//www.51job.com/leshan/">乐山</a></span>
        <span><a href="//www.51job.com/liaocheng/">聊城</a></span>
        <span><a href="//www.51job.com/linfen/">临汾</a></span>
        <span><a href="//www.51job.com/luan/">六安</a></span>
        <span><a href="//www.51job.com/loudi/">娄底</a></span>
        <span><a href="//www.51job.com/luzhou/">泸州</a></span>
        <span><a href="//www.51job.com/luohe/">漯河</a></span>
    </div>
    <div class="e" name="area_channel_div_mnp" style="display:none">
        <span><a href="//www.51job.com/mianyang/">绵阳</a></span>
        <span><a href="//www.51job.com/maanshan/">马鞍山</a></span>
        <span><a href="//www.51job.com/maoming/">茂名</a></span>
        <span><a href="//www.51job.com/meishan/">眉山</a></span>
        <span><a href="//www.51job.com/meizhou/">梅州</a></span>
        <span><a href="//www.51job.com/nanjing/">南京</a></span>
        <span><a href="//www.51job.com/ningbo/">宁波</a></span>
        <span><a href="//www.51job.com/nanchang/">南昌</a></span>
        <span><a href="//www.51job.com/nantong/">南通</a></span>
        <span><a href="//www.51job.com/nanning/">南宁</a></span>
        <span><a href="//www.51job.com/nanchong/">南充</a></span>
        <span><a href="//www.51job.com/nanyang/">南阳</a></span>
        <span><a href="//www.51job.com/neijiang/">内江</a></span>
        <span><a href="//www.51job.com/ningde/">宁德</a></span>
        <span><a href="//www.51job.com/pingdingshan/">平顶山</a></span>
        <span><a href="//www.51job.com/putian/">莆田</a></span>
        <span><a href="//www.51job.com/puyang/">濮阳</a></span>
    </div>
    <div class="e" name="area_channel_div_qrs" style="display:none">
        <span><a href="//www.51job.com/qingdao/">青岛</a></span>
        <span><a href="//www.51job.com/quanzhou/">泉州</a></span>
        <span><a href="//www.51job.com/qinhuangdao/">秦皇岛</a></span>
        <span><a href="//www.51job.com/qingyuan/">清远</a></span>
        <span><a href="//www.51job.com/qiqihaer/">齐齐哈尔</a></span>
        <span><a href="//www.51job.com/quzhou/">衢州</a></span>
        <span><a href="//www.51job.com/qujing/">曲靖</a></span>
        <span><a href="//www.51job.com/rizhao/">日照</a></span>
        <span><a href="//www.51job.com/shanghai/">上海</a></span>
        <span><a href="//www.51job.com/shenzhen/">深圳</a></span>
        <span><a href="//www.51job.com/shenyang/">沈阳</a></span>
        <span><a href="//www.51job.com/shijiazhuang/">石家庄</a></span>
        <span><a href="//www.51job.com/suzhou/">苏州</a></span>
        <span><a href="//www.51job.com/sanya/">三亚</a></span>
        <span><a href="//www.51job.com/shaoxing/">绍兴</a></span>
        <span><a href="//www.51job.com/shantou/">汕头</a></span>
        <span><a href="//www.51job.com/shanwei/">汕尾</a></span>
        <span><a href="//www.51job.com/shangqiu/">商丘</a></span>
        <span><a href="//www.51job.com/shangrao/">上饶</a></span>
        <span><a href="//www.51job.com/shaoguan/">韶关</a></span>
        <span><a href="//www.51job.com/shaoyang/">邵阳</a></span>
        <span><a href="//www.51job.com/shiyan/">十堰</a></span>
        <span><a href="//www.51job.com/suizhou/">随州</a></span>
        <span><a href="//www.51job.com/suining/">遂宁</a></span>
        <span><a href="//www.51job.com/suqian/">宿迁</a></span>
        <span><a href="//www.51job.com/suzhoue/">宿州</a></span>
    </div>
    <div class="e" name="area_channel_div_twx" style="display:none">
        <span><a href="//www.51job.com/tianjin/">天津</a></span>
        <span><a href="//www.51job.com/taiyuan/">太原</a></span>
        <span><a href="//www.51job.com/taizhoue/">台州</a></span>
        <span><a href="//www.51job.com/tangshan/">唐山</a></span>
        <span><a href="//www.51job.com/taizhou/">泰州</a></span>
        <span><a href="//www.51job.com/tieling/">铁岭</a></span>
        <span><a href="//www.51job.com/taian/">泰安</a></span>
        <span><a href="//www.51job.com/wuhan/">武汉</a></span>
        <span><a href="//www.51job.com/wuxi/">无锡</a></span>
        <span><a href="//www.51job.com/wenzhou/">温州</a></span>
        <span><a href="//www.51job.com/urumqi/">乌鲁木齐</a></span>
        <span><a href="//www.51job.com/wuhu/">芜湖</a></span>
        <span><a href="//www.51job.com/weifang/">潍坊</a></span>
        <span><a href="//www.51job.com/weihai/">威海</a></span>
        <span><a href="//www.51job.com/weinan/">渭南</a></span>
        <span><a href="//www.51job.com/xian/">西安</a></span>
        <span><a href="//www.51job.com/xiamen/">厦门</a></span>
        <span><a href="//www.51job.com/xuzhou/">徐州</a></span>
        <span><a href="//www.51job.com/xiangyang/">襄阳</a></span>
        <span><a href="//www.51job.com/xiangtan/">湘潭</a></span>
        <span><a href="//www.51job.com/xianyang/">咸阳</a></span>
        <span><a href="//www.51job.com/xining/">西宁</a></span>
        <span><a href="//www.51job.com/xianning/">咸宁</a></span>
        <span><a href="//www.51job.com/xiaogan/">孝感</a></span>
        <span><a href="//www.51job.com/xinxiang/">新乡</a></span>
        <span><a href="//www.51job.com/xinyang/">信阳</a></span>
        <span><a href="//www.51job.com/xingtai/">邢台</a></span>
        <span><a href="//www.51job.com/xuchang/">许昌</a></span>
        <span><a href="//www.51job.com/xuancheng/">宣城</a></span>
    </div>
    <div class="e" name="area_channel_div_yz" style="display:none">
        <span><a href="//www.51job.com/yantai/">烟台</a></span>
        <span><a href="//www.51job.com/yangzhou/">扬州</a></span>
        <span><a href="//www.51job.com/yichang/">宜昌</a></span>
        <span><a href="//www.51job.com/yancheng/">盐城</a></span>
        <span><a href="//www.51job.com/yiwu/">义乌</a></span>
        <span><a href="//www.51job.com/yingkou/">营口</a></span>
        <span><a href="//www.51job.com/yinchuan/">银川</a></span>
        <span><a href="//www.51job.com/yangjiang/">阳江</a></span>
        <span><a href="//www.51job.com/yibin/">宜宾</a></span>
        <span><a href="//www.51job.com/yichune/">宜春</a></span>
        <span><a href="//www.51job.com/yiyang/">益阳</a></span>
        <span><a href="//www.51job.com/yongzhou/">永州</a></span>
        <span><a href="//www.51job.com/yulin/">玉林</a></span>
        <span><a href="//www.51job.com/yueyang/">岳阳</a></span>
        <span><a href="//www.51job.com/yuncheng/">运城</a></span>
        <span><a href="//www.51job.com/zhangzhou/">漳州</a></span>
        <span><a href="//www.51job.com/zhengzhou/">郑州</a></span>
        <span><a href="//www.51job.com/zhongshan/">中山</a></span>
        <span><a href="//www.51job.com/zhuhai/">珠海</a></span>
        <span><a href="//www.51job.com/zhenjiang/">镇江</a></span>
        <span><a href="//www.51job.com/zhuzhou/">株洲</a></span>
        <span><a href="//www.51job.com/zhanjiang/">湛江</a></span>
        <span><a href="//www.51job.com/zhaoqing/">肇庆</a></span>
        <span><a href="//www.51job.com/zhangjiagang/">张家港</a></span>
        <span><a href="//www.51job.com/zibo/">淄博</a></span>
        <span><a href="//www.51job.com/zaozhuang/">枣庄</a></span>
        <span><a href="//www.51job.com/zhangjiakou/">张家口</a></span>
        <span><a href="//www.51job.com/zhoukou/">周口</a></span>
        <span><a href="//www.51job.com/zhumadian/">驻马店</a></span>
        <span><a href="//www.51job.com/zunyi/">遵义</a></span>
    </div>
            </div>
            <div class="clear"></div>
        </div>
    </div>
</div>

<div id="area_channel_layer_backdrop" class="layer_back_drop_class" style="z-index:999;position:absolute;z-index:999;left:0;top:0;display:none"></div>
<script>

    $(document).ready(function(){
        $(window).resize(function(){
            if(!$("#area_channel_layer").is(":hidden"))
            {
                setLayerPosition();
            }
        });
    });

    window.areaChannelChangeTab = function(sName, oEvent)
    {
        $("#area_channel_layer_all").children().hide();
        $("#area_channel_layer_list").children().removeClass("on");
        $(oEvent).addClass("on");
        $("#area_channel_layer_all").children("div[name='area_channel_div_" + sName + "']").show();
        $("#area_channel_layer_backdrop").show();
    };

    window.openAreaChannelLayer = function()
    {
        setLayerPosition();
        $("#area_channel_layer,#area_channel_layer_backdrop").show();
    };

    window.setLayerPosition = function()
    {
        var dl = $(document).scrollLeft();
        var dt = $(document).scrollTop();
        var ww = $(document).width();
        var dwh = $(document).height();
        var wwh = $(window).height();
        var ow = $("#area_channel_layer").width();
        var oh = $("#area_channel_layer").height();
        var fLeft = (ww - ow) / 2 + dl;
        var fTop = (wwh - oh) * 382 / 1000 + dt;//黄金比例
        $("#area_channel_layer").css({'left': Math.max(parseInt(fLeft), dl), 'top': Math.max(parseInt(fTop), dt)});
        $("#area_channel_layer_backdrop").css({'width': ww + 'px', 'height': dwh + 'px'});
    }
</script>    <div class="nag" id="topIndex">
        <div class="in">
            <a href="//www.51job.com"><img class="logo" id="logo" width="90" height="40" src="//img06.51jobcdn.com/im/2016/logo/logo_blue.png" alt="前程无忧"></a>
                                                                                <img class="slogen" id="slogen" width="162" height="17" src="//img01.51jobcdn.com/im/2016/header/slogen.png?1544426366">
                            
            <!-- Jobs频道使用 start -->
                        <!-- Jobs频道使用 end -->
            
<p class="nlink">
    <a class="" href="//www.51job.com/">首页</a>
    <a class="on" href="https://search.51job.com">职位搜索</a>
    <a class="" href="javascript:openAreaChannelLayer();">地区频道</a>
    <a class="" href="https://mkt.51job.com/careerpost/default_res.php">职场资讯</a>
    <a class="" href="https://xy.51job.com/default-xs.php">校园招聘</a>
    <a href="http://my.51job.com/my/gojingying.php?direct=https%3A%2F%2Fwww.51jingying.com%2Fcommon%2Fsearchcase.php%3F5CC4CE%3D1008" target="_blank">无忧精英</a>
</p>        </div>
    </div>
    <!-- nag end -->
    </div><script>
</script>
<div class="dw_wp">
    <a name="search"></a>
    <input type="hidden" id="pageCode" value="10101">
    <input type="hidden" id="refdomain" value="search.51job.com">
    <input type="hidden" id="refpagecode" value="01">
    <form name="searchForm" method="post" action="" autocomplete="off">
        <input type="hidden" name="lang" value="c">
        <input type="hidden" name="postchannel" value="0000">
        <input type="hidden" name="line" value="">
        <input id="confirmdate" type="hidden" name="confirmdate" value="9">
        <input name="keywordtype" id="keywordtype" type="hidden" value="2">
        <!--搜索条件-->
        <div class="dw_search clearfix Fm">
            <div class="dw_search_in">
                <!-- 全文及相关关键字 -->
                <div class="el on el_q">
                    <ul id="kwdTypeSelUl"><li>全文</li><li><a href="javascript:void(0);" onclick="kwdtypeChangeResult(1);">搜公司</a></li></ul>
                    <p class="ipt">
                        <input type="text" maxlength="200" id="kwdselectid" placeholder="搜索全文/职位名" autocomplete="off" vindex="-1" name="keyword" value="python" class="mytxt at" preval="">
                    </p>
                    <div class="ul" id="KwdSearchResult" style="display:none;">
                    </div>
                    <!--搜索历史 -->
                    <div class="ul" id="searchHistory" style="display:none;z-index: 4;">
    <span class="tl off"><span class="bg b_his">历史记录</span></span>
                        <span class="li" onclick="javascript:window.location.href='https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare='" title="python(全文)+上海">python(全文)+上海</span>
            </div>                </div>
                <!--地点 -->
                <div class="txt pointer" id="work_position_click">
                    <p class="hdl">地点</p>
                    <input autocomplete="off" id="work_position_input" readonly="readonly" type="text" class="ef" placeholder="选择地点" value="上海">
                    <input name="jobarea" id="jobarea" type="hidden" value="020000">
                </div>

                <!-- 行业类别 -->
                <div class="txt pointer long" id="indtype_click">
                    <p class="hdl">行业</p>
                    <input autocomplete="off" id="indtype_input" readonly="readonly" type="text" class="ef" placeholder="选择行业" value="">
                    <input name="industrytype" type="hidden" id="indtype_code" value="">
                </div>
                <!-- 职能类别 -->
                <div class="txt pointer long brn" id="funtype_click">
                    <p class="hdl">职能</p>
                    <input autocomplete="off" id="funtype_input" readonly="readonly" type="text" class="ef" placeholder="选择职能" value="">
                    <input name="funtype" type="hidden" id="funtype_code" value="">
                </div>
                <!-- 搜索按钮 -->
                <button class="p_but" type="button" onclick="search($('#kwdselectid').val(),1)">搜&nbsp;索</button>
            </div>
        <!--搜索条件 END-->
    

    <!--关键字推荐-->
            <div class="dw_recommend">
            <span class="title">猜你喜欢：</span>
            <p>
                                    <a href="https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2B%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" track-type="searchTrackButtonClick" event-type="1" onclick="_tkd.push(['_trackEvent','1511593948209931d4c820d7e7291331733ed54e2248c47b113.100.36.1701pythonPython 开发,Python 高级,Python Web,Python 后端,Python 前端,Python 运维,Python 实习,Python 服务器,Python 爬虫,开发工程师Python 开发']);">Python 开发</a>
                                    <a href="https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2B%25E9%25AB%2598%25E7%25BA%25A7,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" track-type="searchTrackButtonClick" event-type="1" onclick="_tkd.push(['_trackEvent','1511593948209932d4c820d7e7291331733ed54e2248c47b113.100.36.1701pythonPython 开发,Python 高级,Python Web,Python 后端,Python 前端,Python 运维,Python 实习,Python 服务器,Python 爬虫,开发工程师Python 高级']);">Python 高级</a>
                                    <a href="https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2BWeb,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" track-type="searchTrackButtonClick" event-type="1" onclick="_tkd.push(['_trackEvent','1511593948209932d4c820d7e7291331733ed54e2248c47b113.100.36.1701pythonPython 开发,Python 高级,Python Web,Python 后端,Python 前端,Python 运维,Python 实习,Python 服务器,Python 爬虫,开发工程师Python Web']);">Python Web</a>
                                    <a href="https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2B%25E5%2590%258E%25E7%25AB%25AF,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" track-type="searchTrackButtonClick" event-type="1" onclick="_tkd.push(['_trackEvent','1511593948209932d4c820d7e7291331733ed54e2248c47b113.100.36.1701pythonPython 开发,Python 高级,Python Web,Python 后端,Python 前端,Python 运维,Python 实习,Python 服务器,Python 爬虫,开发工程师Python 后端']);">Python 后端</a>
                                    <a href="https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2B%25E5%2589%258D%25E7%25AB%25AF,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" track-type="searchTrackButtonClick" event-type="1" onclick="_tkd.push(['_trackEvent','1511593948209932d4c820d7e7291331733ed54e2248c47b113.100.36.1701pythonPython 开发,Python 高级,Python Web,Python 后端,Python 前端,Python 运维,Python 实习,Python 服务器,Python 爬虫,开发工程师Python 前端']);">Python 前端</a>
                                    <a href="https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2B%25E8%25BF%2590%25E7%25BB%25B4,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" track-type="searchTrackButtonClick" event-type="1" onclick="_tkd.push(['_trackEvent','1511593948209932d4c820d7e7291331733ed54e2248c47b113.100.36.1701pythonPython 开发,Python 高级,Python Web,Python 后端,Python 前端,Python 运维,Python 实习,Python 服务器,Python 爬虫,开发工程师Python 运维']);">Python 运维</a>
                                    <a href="https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2B%25E5%25AE%259E%25E4%25B9%25A0,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" track-type="searchTrackButtonClick" event-type="1" onclick="_tkd.push(['_trackEvent','1511593948209932d4c820d7e7291331733ed54e2248c47b113.100.36.1701pythonPython 开发,Python 高级,Python Web,Python 后端,Python 前端,Python 运维,Python 实习,Python 服务器,Python 爬虫,开发工程师Python 实习']);">Python 实习</a>
                                    <a href="https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2B%25E6%259C%258D%25E5%258A%25A1%25E5%2599%25A8,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" track-type="searchTrackButtonClick" event-type="1" onclick="_tkd.push(['_trackEvent','1511593948209932d4c820d7e7291331733ed54e2248c47b113.100.36.1701pythonPython 开发,Python 高级,Python Web,Python 后端,Python 前端,Python 运维,Python 实习,Python 服务器,Python 爬虫,开发工程师Python 服务器']);">Python 服务器</a>
                                    <a href="https://search.51job.com/list/020000,000000,0000,00,9,99,Python%2B%25E7%2588%25AC%25E8%2599%25AB,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" track-type="searchTrackButtonClick" event-type="1" onclick="_tkd.push(['_trackEvent','1511593948209932d4c820d7e7291331733ed54e2248c47b113.100.36.1701pythonPython 开发,Python 高级,Python Web,Python 后端,Python 前端,Python 运维,Python 实习,Python 服务器,Python 爬虫,开发工程师Python 爬虫']);">Python 爬虫</a>
                                    <a href="https://search.51job.com/list/020000,000000,0000,00,9,99,%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" track-type="searchTrackButtonClick" event-type="1" onclick="_tkd.push(['_trackEvent','1511593948209932d4c820d7e7291331733ed54e2248c47b113.100.36.1701pythonPython 开发,Python 高级,Python Web,Python 后端,Python 前端,Python 运维,Python 实习,Python 服务器,Python 爬虫,开发工程师开发工程师']);">开发工程师</a>
                            </p>
        </div>
        <!--关键字推荐 END-->
</div></form>


    <!--根据关键字和城市展示的广告-->
    
    <!--过滤条件-->
                    
    <div class="dw_filter ">
                    <div class="el mk" id="filter_issuedate">
        <span class="title">发布日期：</span>
                        <ul>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="" class="dw_c_orange" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">所有</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="" class="" href="https://search.51job.com/list/020000,000000,0000,00,0,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">24小时内</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="" class="" href="https://search.51job.com/list/020000,000000,0000,00,1,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">近三天</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="" class="" href="https://search.51job.com/list/020000,000000,0000,00,2,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">近一周</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="" class="" href="https://search.51job.com/list/020000,000000,0000,00,3,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">近一月</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="" class="" href="https://search.51job.com/list/020000,000000,0000,00,4,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">其他</a></li>
                    </ul>
        <div class="clear"></div>
    </div>
        <div class="el on" id="multichoices_issuedate" style="display:none">
        <span class="title">发布日期：</span>
        <ul><li data-value="9" class="on" onclick="checkMultipleChoice(this, 'issuedate')" name="defaultmultichoices"><a href="javascript:void(0)"><em class="check"></em>所有</a></li><li data-value="0" onclick="checkMultipleChoice(this, 'issuedate')"><a href="javascript:void(0)"><em class="check"></em>24小时内</a></li><li data-value="1" onclick="checkMultipleChoice(this, 'issuedate')"><a href="javascript:void(0)"><em class="check"></em>近三天</a></li><li data-value="2" onclick="checkMultipleChoice(this, 'issuedate')"><a href="javascript:void(0)"><em class="check"></em>近一周</a></li><li data-value="3" onclick="checkMultipleChoice(this, 'issuedate')"><a href="javascript:void(0)"><em class="check"></em>近一月</a></li><li data-value="4" onclick="checkMultipleChoice(this, 'issuedate')"><a href="javascript:void(0)"><em class="check"></em>其他</a></li></ul>
        <div class="clear"></div>
        <div class="err" style="display:none">最多只能选择5项</div>
        <div class="btnbox">
            <span class="p_but" track-type="searchTrackButtonClick" event-type="" id="submit_issuedate" onclick="submitMultiChoices('issuedate')">确定</span><span class="p_but gray" onclick="multipleChoiceShow('issuedate', false)">取消</span>
        </div>
    </div>
            <div class="el mk" id="filter_providesalary">
        <span class="title">月薪范围：</span>
                    <span class="more dicon Dm">更多</span>
                            <span class="dx dicon Dm" onclick="multipleChoiceShow('providesalary', true);">多选</span>
                <ul>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="dw_c_orange" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">所有</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,01,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">2千以下</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,02,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">2-3千</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,03,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">3-4.5千</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,04,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">4.5-6千</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,05,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">6-8千</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,06,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">0.8-1万</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,07,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">1-1.5万</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,08,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">1.5-2万</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,09,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">2-3万</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,10,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">3-4万</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,11,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">4-5万</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="20" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,12,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">5万以上</a></li>
                    </ul>
        <div class="clear"></div>
    </div>
        <div class="el on" id="multichoices_providesalary" style="display:none">
        <span class="title">月薪范围：</span>
        <ul><li data-value="99" class="on" onclick="checkMultipleChoice(this, 'providesalary')" name="defaultmultichoices"><a href="javascript:void(0)"><em class="check"></em>所有</a></li><li data-value="01" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>2千以下</a></li><li data-value="02" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>2-3千</a></li><li data-value="03" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>3-4.5千</a></li><li data-value="04" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>4.5-6千</a></li><li data-value="05" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>6-8千</a></li><li data-value="06" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>0.8-1万</a></li><li data-value="07" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>1-1.5万</a></li><li data-value="08" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>1.5-2万</a></li><li data-value="09" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>2-3万</a></li><li data-value="10" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>3-4万</a></li><li data-value="11" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>4-5万</a></li><li data-value="12" onclick="checkMultipleChoice(this, 'providesalary')"><a href="javascript:void(0)"><em class="check"></em>5万以上</a></li></ul>
        <div class="clear"></div>
        <div class="err" style="display:none">最多只能选择5项</div>
        <div class="btnbox">
            <span class="p_but" track-type="searchTrackButtonClick" event-type="20" id="submit_providesalary" onclick="submitMultiChoices('providesalary')">确定</span><span class="p_but gray" onclick="multipleChoiceShow('providesalary', false)">取消</span>
        </div>
    </div>
            <div class="el" id="filter_cotype">
        <span class="title">公司性质：</span>
                    <span class="more dicon Dm">更多</span>
                            <span class="dx dicon Dm" onclick="multipleChoiceShow('cotype', true);">多选</span>
                <ul>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="dw_c_orange" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">所有</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=04&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">国企</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=01&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">外资(欧美)</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=02&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">外资(非欧美)</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=10&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">上市公司</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=03&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">合资</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=05&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">民营公司</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=06&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">外企代表处</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=07&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">政府机关</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=08&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">事业单位</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=09&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">非营利组织</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="21" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=11&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">创业公司</a></li>
                    </ul>
        <div class="clear"></div>
    </div>
        <div class="el on" id="multichoices_cotype" style="display:none">
        <span class="title">公司性质：</span>
        <ul><li data-value="99" class="on" onclick="checkMultipleChoice(this, 'cotype')" name="defaultmultichoices"><a href="javascript:void(0)"><em class="check"></em>所有</a></li><li data-value="04" onclick="checkMultipleChoice(this, 'cotype')"><a href="javascript:void(0)"><em class="check"></em>国企</a></li><li data-value="01" onclick="checkMultipleChoice(this, 'cotype')"><a href="javascript:void(0)"><em class="check"></em>外资(欧美)</a></li><li data-value="02" onclick="checkMultipleChoice(this, 'cotype')"><a href="javascript:void(0)"><em class="check"></em>外资(非欧美)</a></li><li data-value="10" onclick="checkMultipleChoice(this, 'cotype')"><a href="javascript:void(0)"><em class="check"></em>上市公司</a></li><li data-value="03" onclick="checkMultipleChoice(this, 'cotype')"><a href="javascript:void(0)"><em class="check"></em>合资</a></li><li data-value="05" onclick="checkMultipleChoice(this, 'cotype')"><a href="javascript:void(0)"><em class="check"></em>民营公司</a></li><li data-value="06" onclick="checkMultipleChoice(this, 'cotype')"><a href="javascript:void(0)"><em class="check"></em>外企代表处</a></li><li data-value="07" onclick="checkMultipleChoice(this, 'cotype')"><a href="javascript:void(0)"><em class="check"></em>政府机关</a></li><li data-value="08" onclick="checkMultipleChoice(this, 'cotype')"><a href="javascript:void(0)"><em class="check"></em>事业单位</a></li><li data-value="09" onclick="checkMultipleChoice(this, 'cotype')"><a href="javascript:void(0)"><em class="check"></em>非营利组织</a></li><li data-value="11" onclick="checkMultipleChoice(this, 'cotype')"><a href="javascript:void(0)"><em class="check"></em>创业公司</a></li></ul>
        <div class="clear"></div>
        <div class="err" style="display:none">最多只能选择5项</div>
        <div class="btnbox">
            <span class="p_but" track-type="searchTrackButtonClick" event-type="21" id="submit_cotype" onclick="submitMultiChoices('cotype')">确定</span><span class="p_but gray" onclick="multipleChoiceShow('cotype', false)">取消</span>
        </div>
    </div>
            <div class="el" id="filter_workyear">
        <span class="title">工作年限：</span>
                            <span class="dx dicon Dm" onclick="multipleChoiceShow('workyear', true);">多选</span>
                <ul>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="22" class="dw_c_orange" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">所有</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="22" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=01&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">在校生/应届生</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="22" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=02&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">1-3年</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="22" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=03&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">3-5年</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="22" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=04&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">5-10年</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="22" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=05&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">10年以上</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="22" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=06&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">无需经验</a></li>
                    </ul>
        <div class="clear"></div>
    </div>
        <div class="el on" id="multichoices_workyear" style="display:none">
        <span class="title">工作年限：</span>
        <ul><li data-value="99" class="on" onclick="checkMultipleChoice(this, 'workyear')" name="defaultmultichoices"><a href="javascript:void(0)"><em class="check"></em>所有</a></li><li data-value="01" onclick="checkMultipleChoice(this, 'workyear')"><a href="javascript:void(0)"><em class="check"></em>在校生/应届生</a></li><li data-value="02" onclick="checkMultipleChoice(this, 'workyear')"><a href="javascript:void(0)"><em class="check"></em>1-3年</a></li><li data-value="03" onclick="checkMultipleChoice(this, 'workyear')"><a href="javascript:void(0)"><em class="check"></em>3-5年</a></li><li data-value="04" onclick="checkMultipleChoice(this, 'workyear')"><a href="javascript:void(0)"><em class="check"></em>5-10年</a></li><li data-value="05" onclick="checkMultipleChoice(this, 'workyear')"><a href="javascript:void(0)"><em class="check"></em>10年以上</a></li><li data-value="06" onclick="checkMultipleChoice(this, 'workyear')"><a href="javascript:void(0)"><em class="check"></em>无需经验</a></li></ul>
        <div class="clear"></div>
        <div class="err" style="display:none">最多只能选择5项</div>
        <div class="btnbox">
            <span class="p_but" track-type="searchTrackButtonClick" event-type="22" id="submit_workyear" onclick="submitMultiChoices('workyear')">确定</span><span class="p_but gray" onclick="multipleChoiceShow('workyear', false)">取消</span>
        </div>
    </div>
            <div class="el" id="filter_degreefrom">
        <span class="title">学历要求：</span>
                            <span class="dx dicon Dm" onclick="multipleChoiceShow('degreefrom', true);">多选</span>
                <ul>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="23" class="dw_c_orange" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">所有</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="23" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=01&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">初中及以下</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="23" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=02&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">高中/中技/中专</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="23" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=03&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">大专</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="23" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=04&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">本科</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="23" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=05&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">硕士</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="23" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=06&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">博士</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="23" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=07&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">无学历要求</a></li>
                    </ul>
        <div class="clear"></div>
    </div>
        <div class="el on" id="multichoices_degreefrom" style="display:none">
        <span class="title">学历要求：</span>
        <ul><li data-value="99" class="on" onclick="checkMultipleChoice(this, 'degreefrom')" name="defaultmultichoices"><a href="javascript:void(0)"><em class="check"></em>所有</a></li><li data-value="01" onclick="checkMultipleChoice(this, 'degreefrom')"><a href="javascript:void(0)"><em class="check"></em>初中及以下</a></li><li data-value="02" onclick="checkMultipleChoice(this, 'degreefrom')"><a href="javascript:void(0)"><em class="check"></em>高中/中技/中专</a></li><li data-value="03" onclick="checkMultipleChoice(this, 'degreefrom')"><a href="javascript:void(0)"><em class="check"></em>大专</a></li><li data-value="04" onclick="checkMultipleChoice(this, 'degreefrom')"><a href="javascript:void(0)"><em class="check"></em>本科</a></li><li data-value="05" onclick="checkMultipleChoice(this, 'degreefrom')"><a href="javascript:void(0)"><em class="check"></em>硕士</a></li><li data-value="06" onclick="checkMultipleChoice(this, 'degreefrom')"><a href="javascript:void(0)"><em class="check"></em>博士</a></li><li data-value="07" onclick="checkMultipleChoice(this, 'degreefrom')"><a href="javascript:void(0)"><em class="check"></em>无学历要求</a></li></ul>
        <div class="clear"></div>
        <div class="err" style="display:none">最多只能选择5项</div>
        <div class="btnbox">
            <span class="p_but" track-type="searchTrackButtonClick" event-type="23" id="submit_degreefrom" onclick="submitMultiChoices('degreefrom')">确定</span><span class="p_but gray" onclick="multipleChoiceShow('degreefrom', false)">取消</span>
        </div>
    </div>
            <div class="el" id="filter_companysize">
        <span class="title">公司规模：</span>
                            <span class="dx dicon Dm" onclick="multipleChoiceShow('companysize', true);">多选</span>
                <ul>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="24" class="dw_c_orange" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">所有</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="24" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=01&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">少于50人</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="24" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=02&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">50-150人</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="24" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=03&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">150-500人</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="24" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=04&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">500-1000人</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="24" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=05&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">1000-5000人</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="24" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=06&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">5000-10000人</a></li>
                                                            <li><a track-type="searchConditionTrackButtonClick" event-type="24" class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=07&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">10000人以上</a></li>
                    </ul>
        <div class="clear"></div>
    </div>
        <div class="el on" id="multichoices_companysize" style="display:none">
        <span class="title">公司规模：</span>
        <ul><li data-value="99" class="on" onclick="checkMultipleChoice(this, 'companysize')" name="defaultmultichoices"><a href="javascript:void(0)"><em class="check"></em>所有</a></li><li data-value="01" onclick="checkMultipleChoice(this, 'companysize')"><a href="javascript:void(0)"><em class="check"></em>少于50人</a></li><li data-value="02" onclick="checkMultipleChoice(this, 'companysize')"><a href="javascript:void(0)"><em class="check"></em>50-150人</a></li><li data-value="03" onclick="checkMultipleChoice(this, 'companysize')"><a href="javascript:void(0)"><em class="check"></em>150-500人</a></li><li data-value="04" onclick="checkMultipleChoice(this, 'companysize')"><a href="javascript:void(0)"><em class="check"></em>500-1000人</a></li><li data-value="05" onclick="checkMultipleChoice(this, 'companysize')"><a href="javascript:void(0)"><em class="check"></em>1000-5000人</a></li><li data-value="06" onclick="checkMultipleChoice(this, 'companysize')"><a href="javascript:void(0)"><em class="check"></em>5000-10000人</a></li><li data-value="07" onclick="checkMultipleChoice(this, 'companysize')"><a href="javascript:void(0)"><em class="check"></em>10000人以上</a></li></ul>
        <div class="clear"></div>
        <div class="err" style="display:none">最多只能选择5项</div>
        <div class="btnbox">
            <span class="p_but" track-type="searchTrackButtonClick" event-type="24" id="submit_companysize" onclick="submitMultiChoices('companysize')">确定</span><span class="p_but gray" onclick="multipleChoiceShow('companysize', false)">取消</span>
        </div>
    </div>

<div class="el e2 show">
    <span class="title">其他筛选：</span>
    <ul class="ote" id="otherFilter">
                                                        <li track-type="searchTrackButtonClick" event-type="" onclick="showFilterOther('filter_p_keyword', this);">
                                                    <span>薪资福利</span>
                                            </li>
                                                                                    <li track-type="searchTrackButtonClick" event-type="" onclick="showFilterOther('filter_p_jobterm', this);">
                                                    <span>工作类型</span>
                                            </li>
                                                                                    <li track-type="searchTrackButtonClick" event-type="" onclick="showFilterOther('filter_p_jobarea', this);">
                                                    <span>地区地标</span>
                                            </li>
                                                                                                                                    <li track-type="searchTrackButtonClick" event-type="" onclick="showFilterOther('filter_p_line', this);">
                                                    <span>地铁沿线</span>
                                            </li>
                                        </ul>
    <div class="clear"></div>
</div>
<div class="kel" style="display:none;">
        <p id="filter_p_keyword" class="" style="display:none;">
                                                        <a class="dw_c_orange" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">所有</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=01">五险一金</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=02">带薪年假</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=03">节日福利</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=04">周末双休</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=05">绩效奖金</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=06">员工旅游</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=07">立即上岗</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=08">专业培训</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=09">全勤奖</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=10">年终双薪</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=11">定期体检</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=12">交通补贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=13">通讯补贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=14">出差补贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=15">包住</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=16">人才推荐奖</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=17">高温补贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=18">包吃包住</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=19">弹性工作</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=20">补充医疗保险</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=21">年终分红</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=22">免费班车</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=23">出国机会</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=24">住房补贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=25">包吃</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=26">股票期权</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=27">采暖补贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=28">做一休一</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=29">加班补贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=30">餐饮补贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=31">补充公积金</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=32">补充养老保险</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=33">年终奖金</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=34">季度奖金</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=35">团队聚餐</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=36">每年多次调薪</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=37">落户办理</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=38">免息房贷</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=39">全员持股</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=40">子女教育津贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=41">子女保险</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=42">家人免费体检</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=43">家属免费医疗</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=44">外派津贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=45">电脑补助</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=46">油费补贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=47">职位津贴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=48">配车</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=49">不加班</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=50">科研奖励</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=51">在职研究生培养</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=52">健身俱乐部</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=53">探亲假</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=54">母婴室</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=55">做五休二</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=56">做六休一</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=57">无试用期</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=58">工作服</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=59">夫妻房</a>
                                        </p>
        <p id="filter_p_jobterm" class="" style="display:none;">
                                                        <a class="dw_c_orange" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">所有</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=01&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">全职</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=02&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">兼职</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=03&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">实习全职</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=04&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">实习兼职</a>
                                        </p>
        <p id="filter_p_jobarea" class="" style="display:none;">
                                                                                <a class="dw_c_orange" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" onclick="">所有</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showHotdibiaoid(this);return false;">热门地标</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '020100', '', this);return false;">黄浦区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '020300', '', this);return false;">徐汇区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '020400', '', this);return false;">长宁区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '020500', '', this);return false;">静安区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '020600', '', this);return false;">普陀区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '020800', '', this);return false;">虹口区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '020900', '', this);return false;">杨浦区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '021000', '', this);return false;">浦东新区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '021100', '', this);return false;">闵行区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '021200', '', this);return false;">宝山区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '021300', '', this);return false;">嘉定区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '021400', '', this);return false;">金山区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '021500', '', this);return false;">松江区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '021600', '', this);return false;">青浦区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '021800', '', this);return false;">奉贤区</a>
                                                                                <a class="" href="javascript:void(0)" onclick="showDibiaoV('https://search.51job.com', '021900', '', this);return false;">崇明区</a>
                                                            </p>
        <p id="filter_p_dibiaoid" class="nk" style="display:none;">
                                                        <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=56&amp;line=&amp;welfare=">人民广场</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=66&amp;line=&amp;welfare=">徐家汇</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=64&amp;line=&amp;welfare=">五角场</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=69&amp;line=&amp;welfare=">莘庄</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=57&amp;line=&amp;welfare=">上海火车站</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=53&amp;line=&amp;welfare=">陆家嘴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=40&amp;line=&amp;welfare=">八佰伴</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=68&amp;line=&amp;welfare=">中山公园</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=45&amp;line=&amp;welfare=">虹口体育场</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=65&amp;line=&amp;welfare=">新天地</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=51&amp;line=&amp;welfare=">静安寺</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=67&amp;line=&amp;welfare=">张江</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=62&amp;line=&amp;welfare=">外高桥</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=50&amp;line=&amp;welfare=">金桥</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=46&amp;line=&amp;welfare=">虹桥</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=59&amp;line=&amp;welfare=">上海体育场</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=71&amp;line=&amp;welfare=">漕河泾</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=60&amp;line=&amp;welfare=">世纪公园</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=41&amp;line=&amp;welfare=">百盛淮海店</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=44&amp;line=&amp;welfare=">古北新区</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=70&amp;line=&amp;welfare=">闵行经济技术开发区</a>
                                    <a class="" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=52&amp;line=&amp;welfare=">临港新城工业区</a>
                                        </p>
        <p id="filter_p_line" class="" style="display:none;">
                                                        <a class="dw_c_orange" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" onclick="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">所有</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200000100', this);return false;">地铁1号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200000200', this);return false;">地铁2号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200000300', this);return false;">地铁3号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200000400', this);return false;">地铁4号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200000500', this);return false;">地铁5号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200000600', this);return false;">地铁6号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200000700', this);return false;">地铁7号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200000800', this);return false;">地铁8号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200000900', this);return false;">地铁9号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200001000', this);return false;">地铁10号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200001100', this);return false;">地铁11号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200001200', this);return false;">地铁12号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200001300', this);return false;">地铁13号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200001400', this);return false;">地铁16号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200001500', this);return false;">地铁17号线</a>
                                    <a class="" href="javascript:void(0)" onclick="showLineV('https://search.51job.com', '0200001600', this);return false;">地铁浦江线</a>
                                        </p>
    </div>

<!--排除关键字 -->
<div class="el elp" id="">
    <form name="excludeForm" method="post" action="">
        <span class="title">排除关键字：</span>
        <div class="getr">
            <input type="text" name="excludekeyword" placeholder="在结果中排除关键字" maxlength="100" onkeydown="if(event.keyCode==13){return false;}">
            <a href="javascript:void(0);" onclick="excludeword()" track-type="searchTrackButtonClick" event-type="17"><em></em>确定</a>
        </div>
    </form>
</div>
        <div class="op" onclick="collapseExpansionSearch('https://search.51job.com', 'dw_filter', this);">
            <span>展开选项（公司性质、公司规模、工作年限等）<em class="dicon Dm"></em></span>
        </div>
    </div>
    <!--过滤条件 END-->

    <!--已选条件-->
    <div id="dw_choice_mk"></div>
    <div class="dw_choice">
        <div class="in">
            <span class="title">已选条件：</span>
            <p>python(全文)+上海</p>
            <a class="og_but" href="#search">修改</a>
        </div>
    </div>
    <!--已选条件 END-->


    <!--列表表格-->
    <div class="dw_table" id="resultList">
    <!-- 关键字广告 start -->
        <!-- 关键字广告 end -->
    <div id="dw_tlc_mk"></div>
    <div class="dw_tlc">
        <div class="chall">
            <span>
                <em class="check" onclick="selectAllJobs(this, 'delivery_em')" value="" name="select_all" id="top_select_all_jobs_checkbox"></em>
            </span>
            全选
        </div>
        <div class="op">
            <span track-type="searchTrackButtonClick" event-type="13" onclick="delivery('delivery_jobid', '2', '//i.51job.com', 'c', 'https://search.51job.com', '01', '01', '//img03.51jobcdn.com');" class="but_sq uck"><i class="dicon Dm"></i>申请职位</span><span track-type="searchTrackButtonClick" event-type="14" onclick="saveCollection('');" class="but_sc uck"><i class="dicon Dm"></i>收藏职位</span>
        </div>
        <div class="sbox">
            <label>已选：</label>
            <p class="cod at" title="python(全文)+上海">python(全文)+上海</p>
        </div>

        <div class="rt">
    共6793条职位
</div>
<div class="rt">
            <span id="rtPrev" class="dicon Dm"></span>
        <span class="dw_c_orange">1</span>&nbsp;/&nbsp;136            <a href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,2.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=" id="rtNext" class="dicon Dm on"></a>
    </div>



                                                                
        <div class="rt order_time">
            <em class="dicon Dm "></em><a track-type="searchTrackButtonClick" event-type="16" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=1&amp;dibiaoid=0&amp;line=&amp;welfare=">发布时间</a>
        </div>
        <div class="rt order_auto dw_c_orange">
            <em class="dicon Dm  on"></em><a track-type="searchTrackButtonClick" event-type="15" href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">智能排序</a>
        </div>
    </div>

    <!--列表表格 start-->
    <div class="el title">
        <span class="t1">职位名</span>
        <span class="t2">公司名</span>
        <span class="t3">工作地点</span>
        <span class="t4">薪资</span>
        <span class="t5">发布时间</span>
    </div>

        <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="121857920" jt="6" style="display:none">
            <span>
                <a target="_blank" title="数据挖掘工程师" href="https://51rz.51job.com/job.html?jobid=121857920" onmousedown="jobview('121857920');">
                    数据挖掘工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="“前程无忧”51job.com（上海）" href="https://51rz.51job.com/job.html?jobid=71752221&amp;coid=1249">“前程无忧”51job.com（上海）</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4"></span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123035549" jt="0" style="display:none">
            <span>
                <a target="_blank" title="中级Python开发工程师" href="https://jobs.51job.com/shanghai-mhq/123035549.html?s=01&amp;t=0" onmousedown="">
                    中级Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海犇众信息技术有限公司" href="https://jobs.51job.com/all/co3488486.html">上海犇众信息技术有限公司</a></span>
        <span class="t3">上海-闵行区</span>
        <span class="t4">1-1.5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="122805348" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-cnq/122805348.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海凭安征信服务有限公司" href="https://jobs.51job.com/all/co2869172.html">上海凭安征信服务有限公司</a></span>
        <span class="t3">上海-长宁区</span>
        <span class="t4">1.2-2.5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="122765287" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-pdxq/122765287.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海毅朝信息科技有限公司" href="https://jobs.51job.com/all/co2564534.html">上海毅朝信息科技有限公司</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">0.8-1.2万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="122496691" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python 软件开发初级工程师" href="https://jobs.51job.com/shanghai/122496691.html?s=01&amp;t=0" onmousedown="">
                    Python 软件开发初级工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海东软载波微电子有限公司" href="https://jobs.51job.com/all/co129603.html">上海东软载波微电子有限公司</a></span>
        <span class="t3">上海</span>
        <span class="t4"></span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="121503435" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发/深度学习" href="https://jobs.51job.com/shanghai-pdxq/121503435.html?s=01&amp;t=0" onmousedown="">
                    Python开发/深度学习                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海乐野网络科技有限公司" href="https://jobs.51job.com/all/co3947757.html">上海乐野网络科技有限公司</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">1-2万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="114897348" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python/PHP后端程序员" href="https://jobs.51job.com/shanghai-xhq/114897348.html?s=01&amp;t=0" onmousedown="">
                    Python/PHP后端程序员                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海萌果信息科技有限公司" href="https://jobs.51job.com/all/co3087314.html">上海萌果信息科技有限公司</a></span>
        <span class="t3">上海-徐汇区</span>
        <span class="t4">1-1.5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="111232230" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-pdxq/111232230.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="深圳兴融联科技股份有限公司上海分公司" href="https://jobs.51job.com/all/co2759674.html">深圳兴融联科技股份有限公司上海分...</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">1-1.5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123369773" jt="0" style="display:none">
            <span>
                <a target="_blank" title="高级python开发工程师" href="https://jobs.51job.com/shanghai-jdq/123369773.html?s=01&amp;t=0" onmousedown="">
                    高级python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="天津新智视讯技术股份有限公司" href="https://jobs.51job.com/all/co3632501.html">天津新智视讯技术股份有限公司</a></span>
        <span class="t3">上海-嘉定区</span>
        <span class="t4">1.8-2.5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123358525" jt="0" style="display:none">
            <span>
                <a target="_blank" title="资深Python开发工程师" href="https://jobs.51job.com/shanghai-jdq/123358525.html?s=01&amp;t=0" onmousedown="">
                    资深Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海傲觉网络科技有限公司" href="https://jobs.51job.com/all/co5497967.html">上海傲觉网络科技有限公司</a></span>
        <span class="t3">上海-嘉定区</span>
        <span class="t4">2-3.5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123344319" jt="0" style="display:none">
            <span>
                <a target="_blank" title="中高级Python开发工程师" href="https://jobs.51job.com/shanghai/123344319.html?s=01&amp;t=0" onmousedown="">
                    中高级Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="北京汉克时代科技有限公司" href="https://jobs.51job.com/all/co2844997.html">北京汉克时代科技有限公司</a></span>
        <span class="t3">上海</span>
        <span class="t4">1.4-2万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="122842363" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-mhq/122842363.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海名质网络科技有限公司" href="https://jobs.51job.com/all/co4943688.html">上海名质网络科技有限公司</a></span>
        <span class="t3">上海-闵行区</span>
        <span class="t4">1-2万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="122232383" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-xhq/122232383.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="深圳市网新新思软件有限公司" href="https://jobs.51job.com/all/co3749227.html">深圳市网新新思软件有限公司</a></span>
        <span class="t3">上海-徐汇区</span>
        <span class="t4">1-1.5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="117355255" jt="0" style="display:none">
            <span>
                <a target="_blank" title="高级Python算法工程师" href="https://jobs.51job.com/shanghai-jaq/117355255.html?s=01&amp;t=0" onmousedown="">
                    高级Python算法工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="亿翰智库" href="https://jobs.51job.com/all/co3062290.html">亿翰智库</a></span>
        <span class="t3">上海-静安区</span>
        <span class="t4">2-2.5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123179770" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python Engineer" href="https://jobs.51job.com/shanghai/123179770.html?s=01&amp;t=0" onmousedown="">
                    Python Engineer                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="大连华钦软件技术有限公司" href="https://jobs.51job.com/all/co5400670.html">大连华钦软件技术有限公司</a></span>
        <span class="t3">上海</span>
        <span class="t4">1.5-3万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="105294644" jt="0" style="display:none">
            <span>
                <a target="_blank" title="高级Python开发工程师" href="https://jobs.51job.com/shanghai/105294644.html?s=01&amp;t=0" onmousedown="">
                    高级Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="字节跳动" href="https://jobs.51job.com/all/co2758227.html">字节跳动</a></span>
        <span class="t3">上海</span>
        <span class="t4">2.5-5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="122874039" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-pdxq/122874039.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海柯华软件有限公司" href="https://jobs.51job.com/all/co125474.html">上海柯华软件有限公司</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">8-9.5千/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="120963511" jt="0" style="display:none">
            <span>
                <a target="_blank" title="上市医药公司 Python开发工程师" href="https://jobs.51job.com/shanghai-pdxq/120963511.html?s=01&amp;t=0" onmousedown="">
                    上市医药公司 Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="万宝盛华企业管理咨询（上海）有限公司" href="https://jobs.51job.com/all/co5761023.html">万宝盛华企业管理咨询（上海）有限...</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">12-18万/年</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="112471902" jt="0" style="display:none">
            <span>
                <a target="_blank" title="python数据分析师" href="https://jobs.51job.com/shanghai-pdxq/112471902.html?s=01&amp;t=0" onmousedown="">
                    python数据分析师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海澳马信息技术服务有限公司" href="https://jobs.51job.com/all/co1436401.html">上海澳马信息技术服务有限公司</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">1-2万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="118924590" jt="0" style="display:none">
            <span>
                <a target="_blank" title="python开发" href="https://jobs.51job.com/shanghai-pdxq/118924590.html?s=01&amp;t=0" onmousedown="">
                    python开发                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海煜暖实业有限公司" href="https://jobs.51job.com/all/co5643775.html">上海煜暖实业有限公司</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">6-8千/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123307453" jt="0" style="display:none">
            <span>
                <a target="_blank" title="python数据开发工程师" href="https://jobs.51job.com/shanghai-hkq/123307453.html?s=01&amp;t=0" onmousedown="">
                    python数据开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海锐赢信息技术有限公司" href="https://jobs.51job.com/all/co3260759.html">上海锐赢信息技术有限公司</a></span>
        <span class="t3">上海-虹口区</span>
        <span class="t4">1-1.5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="121701741" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai/121701741.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海森松制药设备工程有限公司" href="https://jobs.51job.com/all/co2550408.html">上海森松制药设备工程有限公司</a></span>
        <span class="t3">上海</span>
        <span class="t4">15-20万/年</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123112955" jt="0" style="display:none">
            <span>
                <a target="_blank" title="1131BX-python开发工程师" href="https://jobs.51job.com/shanghai-pdxq/123112955.html?s=01&amp;t=0" onmousedown="">
                    1131BX-python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="平安科技（深圳）有限公司" href="https://jobs.51job.com/all/co2155678.html">平安科技（深圳）有限公司</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">2-2.5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="120097999" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-xhq/120097999.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="中国太平洋保险（集团）股份有限公司" href="https://jobs.51job.com/all/co5419606.html">中国太平洋保险（集团）股份有限公...</a></span>
        <span class="t3">上海-徐汇区</span>
        <span class="t4">15-25万/年</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123329863" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-pdxq/123329863.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="巴乐兔-快乐租房" href="https://jobs.51job.com/all/co3545280.html">巴乐兔-快乐租房</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">1-2万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123316215" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-xhq/123316215.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海舟恩信息技术有限公司" href="https://jobs.51job.com/all/co3400101.html">上海舟恩信息技术有限公司</a></span>
        <span class="t3">上海-徐汇区</span>
        <span class="t4">1.2-1.6万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123138868" jt="0" style="display:none">
            <span>
                <a target="_blank" title="测试开发工程师（python）" href="https://jobs.51job.com/shanghai-xhq/123138868.html?s=01&amp;t=0" onmousedown="">
                    测试开发工程师（python）                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="杉德支付网络服务发展有限公司" href="https://jobs.51job.com/all/co2598882.html">杉德支付网络服务发展有限公司</a></span>
        <span class="t3">上海-徐汇区</span>
        <span class="t4">1-1.5万/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="120436621" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-xhq/120436621.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海牵翼网络科技有限公司" href="https://jobs.51job.com/all/co3698602.html">上海牵翼网络科技有限公司</a></span>
        <span class="t3">上海-徐汇区</span>
        <span class="t4">7-8千/月</span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="115980776" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://51rz.51job.com/job.html?jobid=115980776" onmousedown="jobview('115980776');">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="“前程无忧”51job.com（上海）" href="https://51rz.51job.com/job.html?jobid=71752221&amp;coid=1249">“前程无忧”51job.com（上海）</a></span>
        <span class="t3">上海</span>
        <span class="t4"></span>
        <span class="t5">07-05</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="114088822" jt="0" style="display:none">
            <span>
                <a target="_blank" title="python算法开发" href="https://jobs.51job.com/shanghai-pdxq/114088822.html?s=01&amp;t=0" onmousedown="">
                    python算法开发                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海慧度至明信息科技有限公司" href="https://jobs.51job.com/all/co5518781.html">上海慧度至明信息科技有限公司</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">1-1.5万/月</span>
        <span class="t5">07-04</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="120694247" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师(***)" href="https://jobs.51job.com/shanghai/120694247.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师(***)                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海铠卡医疗器械贸易有限公司" href="https://jobs.51job.com/all/co3962749.html">上海铠卡医疗器械贸易有限公司</a></span>
        <span class="t3">上海</span>
        <span class="t4">1000元/天</span>
        <span class="t5">07-04</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="120029449" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python 高级开发工程师或开发经理" href="https://jobs.51job.com/shanghai/120029449.html?s=01&amp;t=0" onmousedown="">
                    Python 高级开发工程师或开发经理                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="常州汉器信息技术有限公司" href="https://jobs.51job.com/all/co4230517.html">常州汉器信息技术有限公司</a></span>
        <span class="t3">上海</span>
        <span class="t4">1-3万/月</span>
        <span class="t5">07-04</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="122730082" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python高级讲师" href="https://jobs.51job.com/shanghai-pdxq/122730082.html?s=01&amp;t=0" onmousedown="">
                    Python高级讲师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海尚学堂智能科技有限公司" href="https://jobs.51job.com/all/co5187327.html">上海尚学堂智能科技有限公司</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">1-2万/月</span>
        <span class="t5">07-04</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="115310459" jt="0" style="display:none">
            <span>
                <a target="_blank" title="python开发" href="https://jobs.51job.com/shanghai-xhq/115310459.html?s=01&amp;t=0" onmousedown="">
                    python开发                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海坤雷实业有限公司" href="https://jobs.51job.com/all/co5110995.html">上海坤雷实业有限公司</a></span>
        <span class="t3">上海-徐汇区</span>
        <span class="t4">6-8千/月</span>
        <span class="t5">07-04</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="121936358" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-cnq/121936358.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海沪万智能科技有限公司" href="https://jobs.51job.com/all/co3899562.html">上海沪万智能科技有限公司</a></span>
        <span class="t3">上海-长宁区</span>
        <span class="t4">0.7-1.5万/月</span>
        <span class="t5">07-04</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="122647046" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-xhq/122647046.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海悦米信息技术有限公司" href="https://jobs.51job.com/all/co3951454.html">上海悦米信息技术有限公司</a></span>
        <span class="t3">上海-徐汇区</span>
        <span class="t4">1.5-2万/月</span>
        <span class="t5">07-04</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="121371720" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python/Django开发" href="https://jobs.51job.com/shanghai-jaq/121371720.html?s=01&amp;t=0" onmousedown="">
                    Python/Django开发                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海锐成信息科技有限公司" href="https://jobs.51job.com/all/co2812972.html">上海锐成信息科技有限公司</a></span>
        <span class="t3">上海-静安区</span>
        <span class="t4">0.8-1.2万/月</span>
        <span class="t5">07-04</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123279346" jt="0" style="display:none">
            <span>
                <a target="_blank" title="python后端开发工程师" href="https://jobs.51job.com/shanghai-mhq/123279346.html?s=01&amp;t=0" onmousedown="">
                    python后端开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海非夕机器人科技有限公司" href="https://jobs.51job.com/all/co4671974.html">上海非夕机器人科技有限公司</a></span>
        <span class="t3">上海-闵行区</span>
        <span class="t4">1.5-3万/月</span>
        <span class="t5">07-04</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123277415" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-xhq/123277415.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="广州嘉为科技有限公司" href="https://jobs.51job.com/all/co2287694.html">广州嘉为科技有限公司</a></span>
        <span class="t3">上海-徐汇区</span>
        <span class="t4">1-1.5万/月</span>
        <span class="t5">07-04</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="121583766" jt="0" style="display:none">
            <span>
                <a target="_blank" title="python架构师" href="https://jobs.51job.com/shanghai-pdxq/121583766.html?s=01&amp;t=0" onmousedown="">
                    python架构师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="新环康安（深圳）发展有限公司" href="https://jobs.51job.com/all/co4865175.html">新环康安（深圳）发展有限公司</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">1.4-4万/月</span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="121502945" jt="0" style="display:none">
            <span>
                <a target="_blank" title="数据管理工程师(vector SQL python)" href="https://jobs.51job.com/shanghai/121502945.html?s=01&amp;t=0" onmousedown="">
                    数据管理工程师(vector SQL python)                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="高蓓珥派珀管理咨询（上海）有限公司" href="https://jobs.51job.com/all/co3463936.html">高蓓珥派珀管理咨询（上海）有限公...</a></span>
        <span class="t3">上海</span>
        <span class="t4">2-3万/月</span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="122575049" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python技术经理" href="https://jobs.51job.com/shanghai-mhq/122575049.html?s=01&amp;t=0" onmousedown="">
                    Python技术经理                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="聚时科技（上海）有限公司" href="https://jobs.51job.com/all/co5194824.html">聚时科技（上海）有限公司</a></span>
        <span class="t3">上海-闵行区</span>
        <span class="t4">40-50万/年</span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="122129651" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Java爬虫/python爬虫开发工程师" href="https://jobs.51job.com/shanghai-pdxq/122129651.html?s=01&amp;t=0" onmousedown="">
                    Java爬虫/python爬虫开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海新致软件股份有限公司" href="https://jobs.51job.com/all/co156132.html">上海新致软件股份有限公司</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">2-2.5万/月</span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="115319723" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python高级开发工程师" href="https://jobs.51job.com/shanghai/115319723.html?s=01&amp;t=0" onmousedown="">
                    Python高级开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海百趣生物医学科技有限公司" href="https://jobs.51job.com/all/co5333373.html">上海百趣生物医学科技有限公司</a></span>
        <span class="t3">上海</span>
        <span class="t4">1-2.5万/月</span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="120957115" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python高级开发工程师" href="https://jobs.51job.com/shanghai-pdxq/120957115.html?s=01&amp;t=0" onmousedown="">
                    Python高级开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="达观数据" href="https://jobs.51job.com/all/co4133721.html">达观数据</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">1.6-2.5万/月</span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="120532783" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai/120532783.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海占域实业有限公司" href="https://jobs.51job.com/all/co4477690.html">上海占域实业有限公司</a></span>
        <span class="t3">上海</span>
        <span class="t4">6-8千/月</span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="117622468" jt="0" style="display:none">
            <span>
                <a target="_blank" title="python开发" href="https://jobs.51job.com/shanghai-hkq/117622468.html?s=01&amp;t=0" onmousedown="">
                    python开发                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="深圳市若昕科技有限公司" href="https://jobs.51job.com/all/co5613542.html">深圳市若昕科技有限公司</a></span>
        <span class="t3">上海-虹口区</span>
        <span class="t4">2-3万/月</span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="121944519" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-pdxq/121944519.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="HCL Technologies (Shanghai) Limited" href="https://jobs.51job.com/all/co2137128.html">HCL Technologies (Shanghai) Lim...</a></span>
        <span class="t3">上海-浦东新区</span>
        <span class="t4">1.6-2万/月</span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="117307986" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师" href="https://jobs.51job.com/shanghai-mhq/117307986.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海图灵医疗科技有限公司" href="https://jobs.51job.com/all/co2919838.html">上海图灵医疗科技有限公司</a></span>
        <span class="t3">上海-闵行区</span>
        <span class="t4">0.8-1万/月</span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="123022767" jt="0" style="display:none">
            <span>
                <a target="_blank" title="Python开发工程师（英文）" href="https://jobs.51job.com/shanghai-xhq/123022767.html?s=01&amp;t=0" onmousedown="">
                    Python开发工程师（英文）                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="上海伊库伊库网络科技有限公司" href="https://jobs.51job.com/all/co5872598.html">上海伊库伊库网络科技有限公司</a></span>
        <span class="t3">上海-徐汇区</span>
        <span class="t4">1.8-3万/月</span>
        <span class="t5">07-03</span>
    </div>
    <div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="122999465" jt="0" style="display:none">
            <span>
                <a target="_blank" title="高级Python研发工程师" href="https://jobs.51job.com/shanghai-cnq/122999465.html?s=01&amp;t=0" onmousedown="">
                    高级Python研发工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="繁翰信息技术（上海）有限公司" href="https://jobs.51job.com/all/co5367238.html">繁翰信息技术（上海）有限公司</a></span>
        <span class="t3">上海-长宁区</span>
        <span class="t4">2-3万/月</span>
        <span class="t5">07-03</span>
    </div>
    <!--列表表格 END-->
    <div class="dw_line"></div>
    <!--分页-->
    <div class="dw_page">
    <div class="p_box">
        <div class="p_wp">
            <div class="p_in">
                <ul>
                                            <li class="bk"><span>上一页</span></li>
                                                                                            <li class="on">1</li>
                                                                                                <li><a href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,2.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">2</a></li>
                                                                                                <li><a href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,3.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">3</a></li>
                                                                                                <li><a href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,4.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">4</a></li>
                                                                                                <li><a href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,5.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">5</a></li>
                                                                                                <li><a href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,6.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">6</a></li>
                                            
                                            <li class="bk"><a href="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,2.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">下一页</a></li>
                                    </ul>
                <input type="hidden" id="hidTotalPage" value="136">
                <span class="td">共136页，到第</span><input id="jump_page" class="mytxt" type="text" value="1"><span class="td">页</span><span class="og_but" onclick="jumpPage('136');">确定</span>
            </div>
        </div>
    </div>
</div>    <!--分页 END-->

    <div class="clear"></div>
<a href="#top" id="goTop" style="display: none;">回到<br>顶部</a>
<a href="//i.51job.com/userset/advice.php?from=search" target="_blank" class="dw_fb"></a>
    <!-- BANNER 广告 -->
    <div class="mainleft s_search search_btm0">
        <table border="0" cellspacing="0" cellpadding="4"><tbody><tr>
	<td><a adid="33591245" onmousedown="return AdsClick(33591245)" href="https://companyadc.51job.com/companyads/ads/34/33592/33591223/index.htm" title="上海亿通国际股份有限公司" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/images/ads/34/33592/33591245/aa.gif" border="0" width="150" height="60"></a></td>
	<td><a adid="33778137" onmousedown="return AdsClick(33778137)" href="https://companyadc.51job.com/companyads/ads/34/33779/33778078/index.htm" title="苏州柯瑞机械有限公司" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/images/ads/34/33779/33778137/kraa.gif" border="0" width="150" height="60"></a></td>
	<td><a adid="33683731" onmousedown="return AdsClick(33683731)" href="https://companyadc.51job.com/companyads/ads/34/33684/33683660/index.htm" title="深圳波洛斯科技有限公司" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/images/ads/34/33684/33683731/bs.gif" border="0" width="150" height="60"></a></td>
	<td><a adid="33929151" onmousedown="return AdsClick(33929151)" href="https://companyadc.51job.com/companyads/ads/34/33930/33929151/index.htm" title="古驰（中国）贸易有限公司" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/images/ads/34/33930/33929155/gc60.gif" border="0" width="150" height="60"></a></td>
	<td><a adid="33873757" onmousedown="return AdsClick(33873757)" href="https://companyadc.51job.com/companyads/ads/34/33874/33873757/index.htm" title="广州点聚信息科技有限公司" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/images/ads/34/33874/33873757/dj.gif" border="0" width="150" height="60"></a></td>
	<td><a adid="33728677" onmousedown="return AdsClick(33728677)" href="https://companyadc.51job.com/companyads/ads/34/33704/33703724/index.htm" title="深圳市美而佳科技有限公司" target="_blank" onfocus="blur()"><img src="//img05.51jobcdn.com/im/images/ads/34/33729/33728677/mer.gif" border="0" width="150" height="60"></a></td>
</tr>
</tbody></table>    </div>
    <!-- 广告 end -->

    <div class="tResult_bottom_roll  tResult_bottom_roll_w ">
        <!--地区招聘 start -->
        <div class="rollBox">
            <div id="announcement">
    <div id="announcementbody">
                                                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/baotou">包头招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shijiazhuang">石家庄招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tianjin">天津招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taiyuan">太原招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huhhot">呼和浩特招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/baoding">保定招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/langfang">廊坊招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qinhuangdao">秦皇岛招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tangshan">唐山招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/handan">邯郸招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/errduosi">鄂尔多斯招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changchun">长春招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dalian">大连招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shenyang">沈阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/harbin">哈尔滨招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jilin">吉林招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/anshan">鞍山招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yingkou">营口招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/fushun">抚顺招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dandong">丹东招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tieling">铁岭招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/daqing">大庆招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanjing">南京招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanchang">南昌招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/ningbo">宁波招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nantong">南通招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changzhou">常州招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/qingdao">青岛招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/quanzhou">泉州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/suzhou">苏州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shaoxing">绍兴招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/fuzhou">福州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhoue">台州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuxi">无锡招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wenzhou">温州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/hangzhou">杭州招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/hefei">合肥招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiamen">厦门招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xuzhou">徐州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinan">济南招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jiaxing">嘉兴招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinhua">金华招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yantai">烟台招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yangzhou">扬州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunshan">昆山招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/changshu">常熟招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangjiagang">张家港招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yancheng">盐城招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lianyungang">连云港招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huaian">淮安招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhou">泰州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangzhou">漳州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhenjiang">镇江招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/linyi">临沂招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/wuhu">芜湖招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/weifang">潍坊招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/weihai">威海招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huzhou">湖州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yiwu">义乌招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zibo">淄博招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jining">济宁招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanning">南宁招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changsha">长沙招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/dongguan">东莞招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/sanya">三亚招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuhan">武汉招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhengzhou">郑州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhongshan">中山招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuhai">珠海招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/haikou">海口招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/foshan">佛山招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huizhou">惠州招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/jiangmen">江门招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shantou">汕头招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhanjiang">湛江招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qingyuan">清远招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/luoyang">洛阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yichang">宜昌招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangyang">襄阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jingzhou">荆州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuzhou">株洲招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/hengyang">衡阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangtan">湘潭招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changde">常德招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/liuzhou">柳州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chengdu">成都招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chongqing">重庆招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/guiyang">贵阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunming">昆明招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/mianyang">绵阳招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/urumqi">乌鲁木齐招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xian">西安招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lanzhou">兰州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xianyang">咸阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yinchuan">银川招聘</a></li>                </ul>
            
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/baotou">包头人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shijiazhuang">石家庄人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tianjin">天津人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taiyuan">太原人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huhhot">呼和浩特人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/baoding">保定人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/langfang">廊坊人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/qinhuangdao">秦皇岛人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tangshan">唐山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/handan">邯郸人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/errduosi">鄂尔多斯人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changchun">长春人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dalian">大连人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shenyang">沈阳人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/harbin">哈尔滨人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jilin">吉林人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/anshan">鞍山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yingkou">营口人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/fushun">抚顺人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dandong">丹东人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tieling">铁岭人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/daqing">大庆人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanjing">南京人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanchang">南昌人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/ningbo">宁波人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nantong">南通人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changzhou">常州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qingdao">青岛人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/quanzhou">泉州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/suzhou">苏州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shaoxing">绍兴人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/fuzhou">福州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhoue">台州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuxi">无锡人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wenzhou">温州人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/hangzhou">杭州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/hefei">合肥人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiamen">厦门人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xuzhou">徐州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinan">济南人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jiaxing">嘉兴人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinhua">金华人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/yantai">烟台人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yangzhou">扬州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunshan">昆山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changshu">常熟人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangjiagang">张家港人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yancheng">盐城人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lianyungang">连云港人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/huaian">淮安人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhou">泰州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangzhou">漳州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhenjiang">镇江人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/linyi">临沂人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuhu">芜湖人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/weifang">潍坊人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/weihai">威海人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huzhou">湖州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yiwu">义乌人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zibo">淄博人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jining">济宁人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanning">南宁人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changsha">长沙人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/dongguan">东莞人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/sanya">三亚人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuhan">武汉人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhengzhou">郑州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhongshan">中山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuhai">珠海人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/haikou">海口人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/foshan">佛山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huizhou">惠州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jiangmen">江门人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shantou">汕头人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhanjiang">湛江人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qingyuan">清远人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/luoyang">洛阳人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/yichang">宜昌人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangyang">襄阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jingzhou">荆州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuzhou">株洲人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/hengyang">衡阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangtan">湘潭人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changde">常德人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/liuzhou">柳州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chengdu">成都人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chongqing">重庆人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/guiyang">贵阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunming">昆明人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/mianyang">绵阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/urumqi">乌鲁木齐人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/xian">西安人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lanzhou">兰州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xianyang">咸阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yinchuan">银川人才网</a></li>                </ul>
                
                                                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/baotou">包头招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shijiazhuang">石家庄招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tianjin">天津招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taiyuan">太原招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huhhot">呼和浩特招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/baoding">保定招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/langfang">廊坊招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qinhuangdao">秦皇岛招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tangshan">唐山招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/handan">邯郸招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/errduosi">鄂尔多斯招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changchun">长春招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dalian">大连招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shenyang">沈阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/harbin">哈尔滨招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jilin">吉林招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/anshan">鞍山招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yingkou">营口招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/fushun">抚顺招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dandong">丹东招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tieling">铁岭招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/daqing">大庆招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanjing">南京招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanchang">南昌招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/ningbo">宁波招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nantong">南通招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changzhou">常州招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/qingdao">青岛招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/quanzhou">泉州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/suzhou">苏州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shaoxing">绍兴招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/fuzhou">福州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhoue">台州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuxi">无锡招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wenzhou">温州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/hangzhou">杭州招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/hefei">合肥招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiamen">厦门招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xuzhou">徐州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinan">济南招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jiaxing">嘉兴招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinhua">金华招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yantai">烟台招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yangzhou">扬州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunshan">昆山招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/changshu">常熟招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangjiagang">张家港招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yancheng">盐城招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lianyungang">连云港招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huaian">淮安招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhou">泰州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangzhou">漳州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhenjiang">镇江招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/linyi">临沂招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/wuhu">芜湖招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/weifang">潍坊招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/weihai">威海招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huzhou">湖州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yiwu">义乌招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zibo">淄博招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jining">济宁招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanning">南宁招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changsha">长沙招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/dongguan">东莞招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/sanya">三亚招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuhan">武汉招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhengzhou">郑州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhongshan">中山招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuhai">珠海招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/haikou">海口招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/foshan">佛山招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huizhou">惠州招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/jiangmen">江门招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shantou">汕头招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhanjiang">湛江招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qingyuan">清远招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/luoyang">洛阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yichang">宜昌招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangyang">襄阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jingzhou">荆州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuzhou">株洲招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/hengyang">衡阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangtan">湘潭招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changde">常德招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/liuzhou">柳州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chengdu">成都招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chongqing">重庆招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/guiyang">贵阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunming">昆明招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/mianyang">绵阳招聘</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/urumqi">乌鲁木齐招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xian">西安招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lanzhou">兰州招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xianyang">咸阳招聘</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yinchuan">银川招聘</a></li>                </ul>
            
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/baotou">包头人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shijiazhuang">石家庄人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tianjin">天津人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taiyuan">太原人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huhhot">呼和浩特人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/baoding">保定人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/langfang">廊坊人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/qinhuangdao">秦皇岛人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tangshan">唐山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/handan">邯郸人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/errduosi">鄂尔多斯人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changchun">长春人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dalian">大连人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shenyang">沈阳人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/harbin">哈尔滨人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jilin">吉林人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/anshan">鞍山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yingkou">营口人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/fushun">抚顺人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/dandong">丹东人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/tieling">铁岭人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/daqing">大庆人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanjing">南京人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanchang">南昌人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/ningbo">宁波人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nantong">南通人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changzhou">常州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qingdao">青岛人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/quanzhou">泉州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/suzhou">苏州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shaoxing">绍兴人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/fuzhou">福州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhoue">台州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuxi">无锡人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wenzhou">温州人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/hangzhou">杭州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/hefei">合肥人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiamen">厦门人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xuzhou">徐州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinan">济南人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jiaxing">嘉兴人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jinhua">金华人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/yantai">烟台人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yangzhou">扬州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunshan">昆山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changshu">常熟人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangjiagang">张家港人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yancheng">盐城人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lianyungang">连云港人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/huaian">淮安人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/taizhou">泰州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhangzhou">漳州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhenjiang">镇江人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/linyi">临沂人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuhu">芜湖人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/weifang">潍坊人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/weihai">威海人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huzhou">湖州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yiwu">义乌人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zibo">淄博人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jining">济宁人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/nanning">南宁人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changsha">长沙人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/dongguan">东莞人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/sanya">三亚人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/wuhan">武汉人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhengzhou">郑州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhongshan">中山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuhai">珠海人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/haikou">海口人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/foshan">佛山人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/huizhou">惠州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jiangmen">江门人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/shantou">汕头人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhanjiang">湛江人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/qingyuan">清远人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/luoyang">洛阳人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/yichang">宜昌人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangyang">襄阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/jingzhou">荆州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/zhuzhou">株洲人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/hengyang">衡阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xiangtan">湘潭人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/changde">常德人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/liuzhou">柳州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chengdu">成都人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/chongqing">重庆人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/guiyang">贵阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/kunming">昆明人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/mianyang">绵阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/urumqi">乌鲁木齐人才网</a></li>                </ul>
                            <ul><li style="font-size:14px;color:#666;">地区人才网招聘</li>
                    <li class="st_one"><a target="_blank" href="//www.51job.com/xian">西安人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/lanzhou">兰州人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/xianyang">咸阳人才网</a></li><li class="st_one"><a target="_blank" href="//www.51job.com/yinchuan">银川人才网</a></li>                </ul>
                </div>
</div>        </div>
        <!--地区招聘 end-->
        <div class="rollBox">
    <h3>个人简历模版-简历指导</h3>
    <div class="rollBox_twoRow f14">
        <div id="resumeGuideTopicsBody"><div id="marqueeBox" style="overflow:hidden;height:48px"><div><ul class="resumeGuide"><li><a target="_blank" href="//jianli.51job.com/biaoge/" title="个人简历表格"><strong>个人简历表格</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/biaoge/1323.html" title="电子商务专业本科毕业生个人简历表格">电子商务专业...</a></li><li><a target="_blank" href="//jianli.51job.com/xiaohui/" title="高校校徽下载"><strong>高校校徽下载</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/xiaohui/346.html" title="上海理工大学">上海理工大学</a></li><li><a target="_blank" href="//jianli.51job.com/fengmian/" title="简历封面"><strong>简历封面</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/fengmian/9801.html" title="[简历封面下载]激情">[简历封面下载]激...</a></li><li><a target="_blank" href="//jianli.51job.com/gaoxiao/" title="高校简历模板"><strong>高校简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/gaoxiao/211.html" title="杭州师范大学高校简历模版">杭州师范大学...</a></li><li><a target="_blank" href="//jianli.51job.com/zhuanye/" title="专业简历模板"><strong>专业简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/zhuanye/187.html" title="经营管理专业">经营管理专业</a></li><li><a target="_blank" href="//jianli.51job.com/jianliyangben/" title="简历样本"><strong>简历样本</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianliyangben/104.html" title="人力资源总监简历样本">人力资源总监简历...</a></li><li><a target="_blank" href="//jianli.51job.com/jianlifanwen/" title="简历范文"><strong>简历范文</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianlifanwen/14356.html" title="商务总监简历范文">商务总监简历范文</a></li><li><a target="_blank" href="//jianli.51job.com/zhuanye/" title="专业简历模板"><strong>专业简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/zhuanye/192.html" title="广播电视新闻专业">广播电视新闻...</a></li></ul></div><div><ul class="resumeGuide"><li><a target="_blank" href="//jianli.51job.com/biaoge/" title="个人简历表格"><strong>个人简历表格</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/biaoge/1271.html" title="应届毕业生个人简历表格">应届毕业生个...</a></li><li><a target="_blank" href="//jianli.51job.com/gaoxiao/" title="高校简历模板"><strong>高校简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/gaoxiao/128.html" title="同济大学高校简历模版">同济大学高校...</a></li></ul></div></div></div>
        <div id="resumeGuideTopics" style="display:none">
        <div><ul class="resumeGuide"><li><a target="_blank" href="//jianli.51job.com/fengmian/" title="简历封面"><strong>简历封面</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/fengmian/9795.html" title="[简历封面下载]机会">[简历封面下载]机...</a></li><li><a target="_blank" href="//jianli.51job.com/jianlifanwen/" title="简历范文"><strong>简历范文</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianlifanwen/14367.html" title="图书编目加工部主管简历范文">图书编目加工部主...</a></li><li><a target="_blank" href="//jianli.51job.com/biaoge/" title="个人简历表格"><strong>个人简历表格</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/biaoge/1329.html" title="互联网开发个人简历表格">互联网开发个...</a></li><li><a target="_blank" href="//jianli.51job.com/jianliyangben/" title="简历样本"><strong>简历样本</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianliyangben/128.html" title="中国现当代文学简历样本">中国现当代文学简...</a></li><li><a target="_blank" href="//jianli.51job.com/gaoxiao/" title="高校简历模板"><strong>高校简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/gaoxiao/193.html" title="南昌航空大学高校简历模版">南昌航空大学...</a></li><li><a target="_blank" href="//jianli.51job.com/zhuanye/" title="专业简历模板"><strong>专业简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/zhuanye/196.html" title="冶金工程专业">冶金工程专业</a></li><li><a target="_blank" href="//jianli.51job.com/xiaohui/" title="高校校徽下载"><strong>高校校徽下载</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/xiaohui/347.html" title="深圳大学">深圳大学</a></li><li><a target="_blank" href="//jianli.51job.com/jianliyangben/" title="简历样本"><strong>简历样本</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianliyangben/126.html" title="业务员简历样本">业务员简历样本</a></li></ul></div><div><ul class="resumeGuide"><li><a target="_blank" href="//jianli.51job.com/biaoge/" title="个人简历表格"><strong>个人简历表格</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/biaoge/1323.html" title="电子商务专业本科毕业生个人简历表格">电子商务专业...</a></li><li><a target="_blank" href="//jianli.51job.com/xiaohui/" title="高校校徽下载"><strong>高校校徽下载</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/xiaohui/346.html" title="上海理工大学">上海理工大学</a></li><li><a target="_blank" href="//jianli.51job.com/fengmian/" title="简历封面"><strong>简历封面</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/fengmian/9801.html" title="[简历封面下载]激情">[简历封面下载]激...</a></li><li><a target="_blank" href="//jianli.51job.com/gaoxiao/" title="高校简历模板"><strong>高校简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/gaoxiao/211.html" title="杭州师范大学高校简历模版">杭州师范大学...</a></li><li><a target="_blank" href="//jianli.51job.com/zhuanye/" title="专业简历模板"><strong>专业简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/zhuanye/187.html" title="经营管理专业">经营管理专业</a></li><li><a target="_blank" href="//jianli.51job.com/jianliyangben/" title="简历样本"><strong>简历样本</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianliyangben/104.html" title="人力资源总监简历样本">人力资源总监简历...</a></li><li><a target="_blank" href="//jianli.51job.com/jianlifanwen/" title="简历范文"><strong>简历范文</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/jianlifanwen/14356.html" title="商务总监简历范文">商务总监简历范文</a></li><li><a target="_blank" href="//jianli.51job.com/zhuanye/" title="专业简历模板"><strong>专业简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/zhuanye/192.html" title="广播电视新闻专业">广播电视新闻...</a></li></ul></div><div><ul class="resumeGuide"><li><a target="_blank" href="//jianli.51job.com/biaoge/" title="个人简历表格"><strong>个人简历表格</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/biaoge/1271.html" title="应届毕业生个人简历表格">应届毕业生个...</a></li><li><a target="_blank" href="//jianli.51job.com/gaoxiao/" title="高校简历模板"><strong>高校简历模板</strong></a><span style="color:#266EBA"> | </span><a target="_blank" href="//jianli.51job.com/gaoxiao/128.html" title="同济大学高校简历模版">同济大学高校...</a></li></ul></div>        </div>
    </div>
</div>    </div>
    <!-- getPageFormHtml start -->
    <form name="pageForm" action="" method="post" style="display:none">
    <input type="hidden" name="postchannel" value="0000">
    <input type="hidden" name="jobarea" value="020000">
    <input type="hidden" name="district" value="000000">
    <input type="hidden" name="funtype" value="0000">
    <input type="hidden" name="industrytype" value="00">
    <input type="hidden" name="issuedate" value="9">
    <input type="hidden" name="keywordtype" value="2">
    <input type="hidden" name="keyword" value="python">
    <input type="hidden" name="curr_page" value="1">
    <input type="hidden" name="dibiaoid" value="0">
    <input type="hidden" name="line" value="">
    <input type="hidden" name="jobterm" value="99">
    <input type="hidden" name="welfare" value="">
    <input type="hidden" name="workyear" value="99" id="workyear">
    <input type="hidden" name="providesalary" value="99" id="providesalary">
    <input type="hidden" name="cotype" value="99" id="cotype">
    <input type="hidden" name="degreefrom" value="99" id="degreefrom">
    <input type="hidden" name="companysize" value="99" id="companysize">
    <!-- 多选 start -->
    <input type="hidden" name="cotype_tmp" value="99" id="cotype_tmp">
    <input type="hidden" name="workyear_tmp" value="99" id="workyear_tmp">
    <input type="hidden" name="degreefrom_tmp" value="99" id="degreefrom_tmp">
    <input type="hidden" name="companysize_tmp" value="99" id="companysize_tmp">
    <input type="hidden" name="providesalary_tmp" value="99" id="providesalary_tmp">
    <!-- 多选 end -->

    <input type="hidden" name="ord_field" value="0">


    <!-- 由于JS中需要获取该值, 因此给出默认值, 之后全部升级完成, 再从JS中整体的删除 start -->
    <input type="hidden" name="address" value="" id="address">
    <input type="hidden" name="radius" value="-1" id="radius">
    <!-- end -->


    <!-- search start -->
    <input type="hidden" name="jobid_count" value="6793">
    <!-- search end -->

    <input type="hidden" name="pagejump" value="https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,<<pagecode>>.html?lang=c&amp;postchannel=0000&amp;workyear=99&amp;cotype=99&amp;degreefrom=99&amp;jobterm=99&amp;companysize=99&amp;ord_field=0&amp;dibiaoid=0&amp;line=&amp;welfare=">
</form>
    <!-- getPageFormHtml end -->
    <script>
        $(function(){//返回顶部
            var stop='';
            $(window).scroll(function(){
                $('#goTop').hide();
                stop=$(this).scrollTop();
                if(stop>0){
                    $('#goTop').show();
                }else{
                    $('#goTop').hide();
                }
            });
        })
    </script>
    </div>
</div>

<!--引用js-->
<script type="text/javascript" src="//js.51jobcdn.com/in/resource/js/2020/search/common.a8c323f7.js"></script>
<script type="text/javascript" src="//js.51jobcdn.com/in/resource/js/2020/search/searchResult.6a55edcf.js"></script>
<div class="footer">
    <div class="in">
        <div class="nag">
            <div class="e e_first">
                <label>销售热线：</label>400-886-0051&nbsp;&nbsp;027-87810888<br>
                <label>客服热线：</label>400-620-5100<br>
                <label>Email：</label><a href="mailto:club@51job.com" rel="external nofollow">club@51job.com</a>（个人）<br>
                <a href="mailto:hr@51job.com" rel="external nofollow">hr@51job.com</a>（公司）            </div>
            <div class="e">
                <strong>简介</strong><br>
                <a href="//www.51job.com/bo/AboutUs.php" target="_blank">关于我们</a><br>
                <a href="//www.51job.com/bo/service.php" target="_blank">服务声明</a><br>
                <a href="https://media.51job.com/media.php" target="_blank">媒体报道</a><br>
                <a href="https://ir.51job.com/ir/IRMain.php" target="_blank">Investor Relations</a>
            </div>
            <div class="e">
                <strong>合作</strong><br>
                <a href="//www.51job.com/bo/jobs/new_joinus.php" target="_blank">加入我们</a><br>
                <a href="//www.51job.com/bo/contact.php" target="_blank">联系我们</a><br>
                <a href="//www.51job.com/link.php" target="_blank">友情链接</a>            </div>
            <div class="e">
                <strong>帮助</strong><br>
                <a href="https://help.51job.com/home.html" target="_blank">帮助中心</a><br>
                <a href="https://help.51job.com/qa.html?from=b" target="_blank">常见问题</a><br>
                <a href="https://help.51job.com/guide.html?from=d" target="_blank">新手引导</a>            </div>
            <div class="e">
                <strong>导航</strong><br>
                <a href="//www.51job.com/sitemap/site_Navigate.php" target="_blank">网站地图</a><br>
                <a href="https://search.51job.com" target="_blank">职位搜索</a><br>
                <a href="//i.51job.com/resume/resume_center.php?lang=c">简历中心</a><br>
                <a href="//company.51job.com" target="_blank">企业名录</a>            </div>
            <div class="code c_first">
                <img width="80" height="80" src="//img02.51jobcdn.com/im/2016/code/new_app.png" alt="APP下载">
                <span><a href="http://app.51job.com/index.html">APP下载</a></span>
            </div>
            <div class="code">
                <img width="80" height="80" src="//img01.51jobcdn.com/im/2016/code/web_fuwuhao_bottom.png" alt="微信服务号">
                <span>微信服务号</span>
            </div>
            <div class="clear"></div>
        </div>

        <p class="note nag">
            <span>未经51Job同意，不得转载本网站之所有招聘信息及作品 | 无忧工作网版权所有©1999-2020</span>
    </p>    </div>
</div>

</body></html>
"""

from scrapy import  Selector

sel=Selector(text=html)
tag=sel.xpath("//*[@id='resultList']/div[4]/p/span/a/text()").extract()
pass