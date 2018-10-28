//phantom.setProxy('125.70.13.77', '8080', 'sock5');
phantom.cookiesEnabled= true;
phantom.clearCookies();
xxx = phantom.addCookie({
  'path': '/',
  'name': 'HMVT',
  'value': '',
  'domain': 'hm.baidu.com',
  'expires'  : (new Date()).getTime() + (1000 * 60 * 60)
})
yyy=phantom.addCookie({
  'name': 'HMACCOUNT',
  'value': '',
  'domain': 'hm.baidu.com'
})
zzz=phantom.addCookie({
  'name': 'Hm_lpvt_f6378f30c952781c24d9f9819e1f5ee1',
  'value': '',
  'domain': 'jiaoda7.com'
})
aaa=phantom.addCookie({
  'name': 'Hm_lvt_f6378f30c952781c24d9f9819e1f5ee1',
  'value': '',
  'domain': 'jiaoda7.com'
})

console.log(xxx)
console.log(yyy)
console.log(zzz)
console.log(aaa)


// console.log(phantom.cookies[0].name)
// console.log(phantom.cookies[1].name)
// console.log(phantom.cookies[2].name)
// console.log(phantom.cookies[3].name)
// console.log(phantom.cookies[0].value)
// console.log(phantom.cookies[1].value)
// console.log(phantom.cookies[2].value)
// console.log(phantom.cookies[3].value)
// console.log(phantom.cookies[0].domain)
// console.log(phantom.cookies[1].domain)
// console.log(phantom.cookies[2].domain)
// console.log(phantom.cookies[3].domain)



var page = require('webpage').create();
//page.settings.userAgent = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; 360SE)"
// page.onResourceRequested = function(requestData, networkRequest) {
//     console.log('Request (#' + requestData.id + '): ' + JSON.stringify(requestData));
// };
page.cookiesEnabled=true;
page.open('http://jiaoda7.com/',function(status) {
  console.log(status)
  console.log(page.title)
  for (var i = 0; i < page.cookies.length; i++) {
      console.log(page.cookies[i].name + "=" + page.cookies[i].value);
  }
  setTimeout(function(){
    page.close();
    phantom.exit();
  },5000)
});


