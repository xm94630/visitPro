phantom.setProxy('125.70.13.77', '8080', 'sock5');
phantom.cookiesEnabled= false;
phantom.clearCookies();
xxx = phantom.addCookie({
  'path': '/',
  'name': 'HMVT',
  'value': '1',
  'domain': '.hm.baidu.com',
  'expires'  : (new Date()).getTime() + (1000 * 60 * 60)
})
yyy = phantom.addCookie({
  'name'     : 'Valid-Cookie-Name',   /* required property */
  'value'    : 'Valid-Cookie-Value',  /* required property */
  'domain'   : 'localhost',
  'path'     : '/foo',                /* required property */
  'httponly' : true,
  'secure'   : false,
  'expires'  : (new Date()).getTime() + (1000 * 60 * 60)   /* <-- expires in 1 hour */
});
console.log(xxx)
console.log(yyy)
phantom.addCookie({
  'name': 'HMACCOUNT',
  'value': '2',
  'domain': '.hm.baidu.com'
})
phantom.addCookie({
  'name': 'Hm_lpvt_f6378f30c952781c24d9f9819e1f5ee1',
  'value': '3',
  'domain': '.jiaoda7.com'
})
phantom.addCookie({
  'name': 'Hm_lvt_f6378f30c952781c24d9f9819e1f5ee1',
  'value': '4',
  'domain': '.jiaoda7.com'
})
console.log('Listing cookies1:');
console.log(phantom.cookies);
for(var i in phantom.cookies) {
    console.log('==>')
   console.log(cookies[i].name + '=' + cookies[i].value);
}



var page = require('webpage').create();
page.settings.userAgent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; 360SE)"
page.cookiesEnabled = false
page.clearCookies();
console.log('Listing cookies2:');
for(var i in page.cookies) {
    console.log('==>')
   console.log(cookies[i].name + '=' + cookies[i].value);
}

page.onInitialized = function () {
  console.log(123123123)
  var userAgent = window.navigator.userAgent,
  platform = window.navigator.platform;
window.navigator.cookieEnabled = true;
window.localStorage.setItem("Hm_lvt_f6378f30c952781c24d9f9819e1f5ee1", "");
window.localStorage.clear();
console.log(localStorage.length)
};



page.onResourceRequested = function(requestData, networkRequest) {
    console.log('Request (#' + requestData.id + '): ' + JSON.stringify(requestData));
};

page.open('http://jiaoda7.com/',function(status) {

  console.log(status)
  console.log(page.title)
  console.log(window.localStorage)
  console.log(window.localStorage.length)
  console.log('Listing cookies3:');
  for(var i in page.cookies) {
      console.log('==>')
    console.log(cookies[i].name + '=' + cookies[i].value);
  }
  for(var i in phantom.cookies) {
    console.log('==>')
    console.log(cookies[i].name + '=' + cookies[i].value);
  }
  setTimeout(function(){
    //page.clearCookies()
    //phantom.clearCookies();
    page.close();
    phantom.exit();
  },500000)
});


