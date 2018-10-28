// var page = require('webpage').create(),
//     system = require('system'),
//     host, port;



// host = 'http://125.70.13.77';
// port = '8080';
// phantom.setProxy(host, port, 'manual', '', '');



// var page = require('webpage').create(),
//     server = 'http://www.jiado7.com',
//     data = '';

// page.open(server, 'post', data, function (status) {
//     if (status !== 'success') {
//         console.log('Unable to post!');
//     } else {
//         console.log(page.content);
//     }
//     phantom.exit();
// });




var page = require('webpage').create();
// 不要用这个
page.customHeaders = {};

//page.settings.userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36";
//page.settings.userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
page.settings.userAgent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; 360SE)"
//page.settings.userAgent = "Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/4.1 Mobile Safari/533.1"
//page.settings.userAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12A365 MicroMessenger/5.4.1 NetType/WIFI",


//这样子写是无效的
//page.settings.Host = 'jiaoda7.com'


settings = {
    headers: {
        "Referer": "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E4%BA%A4%E5%A4%A7%E7%BE%A4%E4%BE%A0%E4%BC%A0%20%E9%BB%84%E9%87%91%E7%89%88&oq=%25E4%25BA%25A4%25E5%25A4%25A7%25E7%25BE%25A4%25E4%25BE%25A0%25E4%25BC%25A0%2520%25E9%25BB%2584%25E9%2587%2591%25E7%2589%2588&rsv_pq=dcf0970e00001b4f&rsv_t=9875rS%2F1WIV1KrSNnCBwRlsvmaRfrw2XPafFOSS8x864Vknj0ZgP4Tx4uqE&rqlang=cn&rsv_enter=0",
        'Origin': 'http://www.jiaoda7.com',
        Accept: "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,fr;q=0.5",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
        //Cookie: "Hm_lvt_f6378f30c952781c24d9f9819e1f5ee1=1540535500,1540535862,1540535954,1540536057; Hm_lpvt_f6378f30c952781c24d9f9819e1f5ee1=1540536057",
        Host: "jiaoda7.com",
        Pragma: "no-cache",
        "Upgrade-Insecure-Requests": 1,
    }
};

phantom.setProxy('125.70.13.77', '8080', 'sock5');
//phantom.setProxy('114.113.126.86', '80', 'manual');//北京 透明代理，显示的还是上海的，百度统计识别为老访客

//phantom.setProxy('222.221.11.119', '3218', 'manual', '', '');//云南昆明 透明 有点慢
//phantom.setProxy('61.138.33.20', '808', 'manual', '', '');//七里河 有点慢

//phantom.setProxy('115.151.2.154', '808', 'manual', '', '');//江西宜春 高匿



page.clearCookies()


console.log('Listing cookies1:');
console.log(phantom.cookies)
console.log('++.11')
for(var i in phantom.cookies) {
    console.log('==>')
   console.log(cookies[i].name + '=' + cookies[i].value);
}


page.onResourceRequested = function(requestData, networkRequest) {
    console.log('Request (#' + requestData.id + '): ' + JSON.stringify(requestData));
};
page.open('http://jiaoda7.com/', settings,function(status) {
  console.log(status)
  console.log(page.title)

  var cookies = page.cookies;

  page.deleteCookie('Hm_lpvt_f6378f30c952781c24d9f9819e1f5ee1');
  page.deleteCookie('Hm_lvt_f6378f30c952781c24d9f9819e1f5ee1');
  page.clearCookies()
  console.log('Listing cookies2:');


  phantom.clearCookies();
  for(var i in phantom.cookies) {
      console.log('==>')
    console.log(cookies[i].name + '=' + cookies[i].value);
  }


  //page.render('yyy.png');

//   setTimeout(function(){
//     // page.includeJs("http://libs.baidu.com/jquery/2.0.0/jquery.min.js", function() {
//     //     page.evaluate(function() {
//     //       $($(".gameBoxR a")[0]).click();
//     //     });
//     //     phantom.exit()
//     // });


//     page.open('https://jiaoda7.gitee.io/myweb/game/jiaoda2_gold/index.html',function() {
//         console.log('page opened2');
//         setTimeout(function(){
//             page.close();
//             setTimeout(function(){
//                 phantom.exit();
//             },5000)
//         },5000)
//     });
//   },3000)

    setTimeout(function(){
        page.close();
        setTimeout(function(){
            phantom.exit();
        },2000)
    },5000)

  
});
page.onClosing = function(closingPage) {
    console.log('The page is closing! URL: ' + closingPage.url);
};