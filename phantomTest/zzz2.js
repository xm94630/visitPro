phantom.setProxy('125.70.13.77', '8080', 'sock5');
phantom.cookiesEnabled= true;
phantom.clearCookies();
phantom.addCookie({
  'name': 'HMVT',
  'value': '',
  'domain': '.hm.baidu.com'
})
phantom.addCookie({
  'name': 'HMACCOUNT',
  'value': '',
  'domain': '.hm.baidu.com'
})
phantom.addCookie({
  'name': 'Hm_lpvt_f6378f30c952781c24d9f9819e1f5ee1',
  'value': '',
  'domain': '.jiaoda7.com'
})
phantom.addCookie({
  'name': 'Hm_lvt_f6378f30c952781c24d9f9819e1f5ee1',
  'value': '',
  'domain': '.jiaoda7.com'
})


var page = require('webpage').create();
page.settings.userAgent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; 360SE)"
// page.cookiesEnabled = false
// page.clearCookies();


// page.onResourceRequested = function(requestData, networkRequest) {
//     console.log('Request (#' + requestData.id + '): ' + JSON.stringify(requestData));
// };

page.open('http://jiaoda7.com/',function(status) {
  console.log(status)
  console.log(page.title)
  setTimeout(function(){
    page.close();
    phantom.exit();
  },3000)
});


