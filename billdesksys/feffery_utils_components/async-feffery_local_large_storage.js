(window.webpackJsonpfeffery_utils_components=window.webpackJsonpfeffery_utils_components||[]).push([[20],{506:function(e,t,n){n.r(t);var i=n(1),a=n.n(i),r=n(205),o=n(736),c=n.n(o),u=n(25);function x(e){return(x="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function O(){O=function(){return a};var u,a={},e=Object.prototype,f=e.hasOwnProperty,s=Object.defineProperty||function(e,t,n){e[t]=n.value},t="function"==typeof Symbol?Symbol:{},r=t.iterator||"@@iterator",n=t.asyncIterator||"@@asyncIterator",o=t.toStringTag||"@@toStringTag";function i(e,t,n){return Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}),e[t]}try{i({},"")}catch(u){i=function(e,t,n){return e[t]=n}}function c(e,t,n,r){var o,i,a,c,t=t&&t.prototype instanceof y?t:y,t=Object.create(t.prototype),r=new N(r||[]);return s(t,"_invoke",{value:(o=e,i=n,a=r,c=d,function(e,t){if(c===h)throw Error("Generator is already running");if(c===v){if("throw"===e)throw t;return{value:u,done:!0}}for(a.method=e,a.arg=t;;){var n=a.delegate;if(n){n=function e(t,n){var r=n.method,o=t.iterator[r];if(o===u)return n.delegate=null,"throw"===r&&t.iterator.return&&(n.method="return",n.arg=u,e(t,n),"throw"===n.method)||"return"!==r&&(n.method="throw",n.arg=new TypeError("The iterator does not provide a '"+r+"' method")),p;r=l(o,t.iterator,n.arg);if("throw"===r.type)return n.method="throw",n.arg=r.arg,n.delegate=null,p;o=r.arg;return o?o.done?(n[t.resultName]=o.value,n.next=t.nextLoc,"return"!==n.method&&(n.method="next",n.arg=u),n.delegate=null,p):o:(n.method="throw",n.arg=new TypeError("iterator result is not an object"),n.delegate=null,p)}(n,a);if(n){if(n===p)continue;return n}}if("next"===a.method)a.sent=a._sent=a.arg;else if("throw"===a.method){if(c===d)throw c=v,a.arg;a.dispatchException(a.arg)}else"return"===a.method&&a.abrupt("return",a.arg);c=h;n=l(o,i,a);if("normal"===n.type){if(c=a.done?v:"suspendedYield",n.arg===p)continue;return{value:n.arg,done:a.done}}"throw"===n.type&&(c=v,a.method="throw",a.arg=n.arg)}})}),t}function l(e,t,n){try{return{type:"normal",arg:e.call(t,n)}}catch(e){return{type:"throw",arg:e}}}a.wrap=c;var d="suspendedStart",h="executing",v="completed",p={};function y(){}function b(){}function m(){}var t={},g=(i(t,r,function(){return this}),Object.getPrototypeOf),g=g&&g(g(j([]))),_=(g&&g!==e&&f.call(g,r)&&(t=g),m.prototype=y.prototype=Object.create(t));function w(e){["next","throw","return"].forEach(function(t){i(e,t,function(e){return this._invoke(t,e)})})}function I(a,c){var t;s(this,"_invoke",{value:function(n,r){function e(){return new c(function(e,t){!function t(e,n,r,o){var i,e=l(a[e],a,n);if("throw"!==e.type)return(n=(i=e.arg).value)&&"object"==x(n)&&f.call(n,"__await")?c.resolve(n.__await).then(function(e){t("next",e,r,o)},function(e){t("throw",e,r,o)}):c.resolve(n).then(function(e){i.value=e,r(i)},function(e){return t("throw",e,r,o)});o(e.arg)}(n,r,e,t)})}return t=t?t.then(e,e):e()}})}function S(e){var t={tryLoc:e[0]};1 in e&&(t.catchLoc=e[1]),2 in e&&(t.finallyLoc=e[2],t.afterLoc=e[3]),this.tryEntries.push(t)}function E(e){var t=e.completion||{};t.type="normal",delete t.arg,e.completion=t}function N(e){this.tryEntries=[{tryLoc:"root"}],e.forEach(S,this),this.reset(!0)}function j(t){if(t||""===t){var n,e=t[r];if(e)return e.call(t);if("function"==typeof t.next)return t;if(!isNaN(t.length))return n=-1,(e=function e(){for(;++n<t.length;)if(f.call(t,n))return e.value=t[n],e.done=!1,e;return e.value=u,e.done=!0,e}).next=e}throw new TypeError(x(t)+" is not iterable")}return s(_,"constructor",{value:b.prototype=m,configurable:!0}),s(m,"constructor",{value:b,configurable:!0}),b.displayName=i(m,o,"GeneratorFunction"),a.isGeneratorFunction=function(e){e="function"==typeof e&&e.constructor;return!!e&&(e===b||"GeneratorFunction"===(e.displayName||e.name))},a.mark=function(e){return Object.setPrototypeOf?Object.setPrototypeOf(e,m):(e.__proto__=m,i(e,o,"GeneratorFunction")),e.prototype=Object.create(_),e},a.awrap=function(e){return{__await:e}},w(I.prototype),i(I.prototype,n,function(){return this}),a.AsyncIterator=I,a.async=function(e,t,n,r,o){void 0===o&&(o=Promise);var i=new I(c(e,t,n,r),o);return a.isGeneratorFunction(t)?i:i.next().then(function(e){return e.done?e.value:i.next()})},w(_),i(_,o,"Generator"),i(_,r,function(){return this}),i(_,"toString",function(){return"[object Generator]"}),a.keys=function(e){var t,n=Object(e),r=[];for(t in n)r.push(t);return r.reverse(),function e(){for(;r.length;){var t=r.pop();if(t in n)return e.value=t,e.done=!1,e}return e.done=!0,e}},a.values=j,N.prototype={constructor:N,reset:function(e){if(this.prev=0,this.next=0,this.sent=this._sent=u,this.done=!1,this.delegate=null,this.method="next",this.arg=u,this.tryEntries.forEach(E),!e)for(var t in this)"t"===t.charAt(0)&&f.call(this,t)&&!isNaN(+t.slice(1))&&(this[t]=u)},stop:function(){this.done=!0;var e=this.tryEntries[0].completion;if("throw"===e.type)throw e.arg;return this.rval},dispatchException:function(n){if(this.done)throw n;var r=this;function e(e,t){return i.type="throw",i.arg=n,r.next=e,t&&(r.method="next",r.arg=u),!!t}for(var t=this.tryEntries.length-1;0<=t;--t){var o=this.tryEntries[t],i=o.completion;if("root"===o.tryLoc)return e("end");if(o.tryLoc<=this.prev){var a=f.call(o,"catchLoc"),c=f.call(o,"finallyLoc");if(a&&c){if(this.prev<o.catchLoc)return e(o.catchLoc,!0);if(this.prev<o.finallyLoc)return e(o.finallyLoc)}else if(a){if(this.prev<o.catchLoc)return e(o.catchLoc,!0)}else{if(!c)throw Error("try statement without catch or finally");if(this.prev<o.finallyLoc)return e(o.finallyLoc)}}}},abrupt:function(e,t){for(var n=this.tryEntries.length-1;0<=n;--n){var r=this.tryEntries[n];if(r.tryLoc<=this.prev&&f.call(r,"finallyLoc")&&this.prev<r.finallyLoc){var o=r;break}}var i=(o=o&&("break"===e||"continue"===e)&&o.tryLoc<=t&&t<=o.finallyLoc?null:o)?o.completion:{};return i.type=e,i.arg=t,o?(this.method="next",this.next=o.finallyLoc,p):this.complete(i)},complete:function(e,t){if("throw"===e.type)throw e.arg;return"break"===e.type||"continue"===e.type?this.next=e.arg:"return"===e.type?(this.rval=this.arg=e.arg,this.method="return",this.next="end"):"normal"===e.type&&t&&(this.next=t),p},finish:function(e){for(var t=this.tryEntries.length-1;0<=t;--t){var n=this.tryEntries[t];if(n.finallyLoc===e)return this.complete(n.completion,n.afterLoc),E(n),p}},catch:function(e){for(var t=this.tryEntries.length-1;0<=t;--t){var n,r,o=this.tryEntries[t];if(o.tryLoc===e)return"throw"===(n=o.completion).type&&(r=n.arg,E(o)),r}throw Error("illegal catch attempt")},delegateYield:function(e,t,n){return this.delegate={iterator:j(e),resultName:t,nextLoc:n},"next"===this.method&&(this.arg=u),p}},a}function f(e,t,n,r,o,i,a){try{var c=e[i](a),u=c.value}catch(e){return n(e)}c.done?t(u):Promise.resolve(u).then(r,o)}function s(c){return function(){var e=this,a=arguments;return new Promise(function(t,n){var r=c.apply(e,a);function o(e){f(r,t,n,o,i,"next",e)}function i(e){f(r,t,n,o,i,"throw",e)}o(void 0)})}}function l(e){var n=e.id,t=e.data,r=e.initialSync,o=e.setProps;return e.loading_state,Object(i.useEffect)(function(){s(O().mark(function e(){var t;return O().wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(r)return e.prev=1,e.next=4,c.a.getItem(n);e.next=11;break;case 4:(t=e.sent)&&o({data:JSON.parse(t)}),e.next=11;break;case 8:e.prev=8,e.t0=e.catch(1),console.error(e.t0);case 11:case"end":return e.stop()}},e,null,[[1,8]])}))()},[]),Object(i.useEffect)(function(){s(O().mark(function e(){return O().wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(Object(u.isUndefined)(t)){e.next=9;break}return e.prev=1,e.next=4,c.a.setItem(n,JSON.stringify(t));case 4:e.next=9;break;case 6:e.prev=6,e.t0=e.catch(1),console.error(e.t0);case 9:case"end":return e.stop()}},e,null,[[1,6]])}))()},[t]),a.a.createElement(a.a.Fragment,null)}t.default=a.a.memo(l),l.defaultProps=r.b,l.propTypes=r.c},736:function(e,t,n){!function(r){e.exports=function r(o,i,a){function c(t,e){if(!i[t]){if(!o[t])throw(n=new Error("Cannot find module '"+t+"'")).code="MODULE_NOT_FOUND",n;var n=i[t]={exports:{}};o[t][0].call(n.exports,function(e){return c(o[t][1][e]||e)},n,n.exports,r,o,i,a)}return i[t].exports}for(var e=0;e<a.length;e++)c(a[e]);return c}({1:[function(e,f,t){!function(t){var r,e,n,o,i=t.MutationObserver||t.WebKitMutationObserver,a=i?(e=0,i=new i(u),n=t.document.createTextNode(""),i.observe(n,{characterData:!0}),function(){n.data=e=++e%2}):t.setImmediate||void 0===t.MessageChannel?"document"in t&&"onreadystatechange"in t.document.createElement("script")?function(){var e=t.document.createElement("script");e.onreadystatechange=function(){u(),e.onreadystatechange=null,e.parentNode.removeChild(e),e=null},t.document.documentElement.appendChild(e)}:function(){setTimeout(u,0)}:((o=new t.MessageChannel).port1.onmessage=u,function(){o.port2.postMessage(0)}),c=[];function u(){var e,t;r=!0;for(var n=c.length;n;){for(t=c,c=[],e=-1;++e<n;)t[e]();n=c.length}r=!1}f.exports=function(e){1!==c.push(e)||r||a()}}.call(this,void 0!==r?r:"undefined"!=typeof self?self:"undefined"!=typeof window?window:{})},{}],2:[function(e,t,n){var o=e(1);function u(){}var f={},i=["REJECTED"],a=["FULFILLED"],r=["PENDING"];function c(e){if("function"!=typeof e)throw new TypeError("resolver must be a function");this.state=r,this.queue=[],this.outcome=void 0,e!==u&&h(this,e)}function s(e,t,n){this.promise=e,"function"==typeof t&&(this.onFulfilled=t,this.callFulfilled=this.otherCallFulfilled),"function"==typeof n&&(this.onRejected=n,this.callRejected=this.otherCallRejected)}function l(t,n,r){o(function(){var e;try{e=n(r)}catch(e){return f.reject(t,e)}e===t?f.reject(t,new TypeError("Cannot resolve promise with itself")):f.resolve(t,e)})}function d(e){var t=e&&e.then;if(e&&("object"==typeof e||"function"==typeof e)&&"function"==typeof t)return function(){t.apply(e,arguments)}}function h(t,e){var n=!1;function r(e){n||(n=!0,f.reject(t,e))}function o(e){n||(n=!0,f.resolve(t,e))}var i=v(function(){e(o,r)});"error"===i.status&&r(i.value)}function v(e,t){var n={};try{n.value=e(t),n.status="success"}catch(e){n.status="error",n.value=e}return n}(t.exports=c).prototype.catch=function(e){return this.then(null,e)},c.prototype.then=function(e,t){var n;return"function"!=typeof e&&this.state===a||"function"!=typeof t&&this.state===i?this:(n=new this.constructor(u),this.state!==r?l(n,this.state===a?e:t,this.outcome):this.queue.push(new s(n,e,t)),n)},s.prototype.callFulfilled=function(e){f.resolve(this.promise,e)},s.prototype.otherCallFulfilled=function(e){l(this.promise,this.onFulfilled,e)},s.prototype.callRejected=function(e){f.reject(this.promise,e)},s.prototype.otherCallRejected=function(e){l(this.promise,this.onRejected,e)},f.resolve=function(e,t){var n=v(d,t);if("error"===n.status)return f.reject(e,n.value);n=n.value;if(n)h(e,n);else{e.state=a,e.outcome=t;for(var r=-1,o=e.queue.length;++r<o;)e.queue[r].callFulfilled(t)}return e},f.reject=function(e,t){e.state=i,e.outcome=t;for(var n=-1,r=e.queue.length;++n<r;)e.queue[n].callRejected(t);return e},c.resolve=function(e){return e instanceof this?e:f.resolve(new this(u),e)},c.reject=function(e){var t=new this(u);return f.reject(t,e)},c.all=function(e){var n=this;if("[object Array]"!==Object.prototype.toString.call(e))return this.reject(new TypeError("must be an array"));var r=e.length,o=!1;if(!r)return this.resolve([]);for(var i=new Array(r),a=0,t=-1,c=new this(u);++t<r;)!function(e,t){n.resolve(e).then(function(e){i[t]=e,++a!==r||o||(o=!0,f.resolve(c,i))},function(e){o||(o=!0,f.reject(c,e))})}(e[t],t);return c},c.race=function(e){if("[object Array]"!==Object.prototype.toString.call(e))return this.reject(new TypeError("must be an array"));var t=e.length,n=!1;if(!t)return this.resolve([]);for(var r,o=-1,i=new this(u);++o<t;)r=e[o],this.resolve(r).then(function(e){n||(n=!0,f.resolve(i,e))},function(e){n||(n=!0,f.reject(i,e))});return i}},{1:1}],3:[function(t,e,n){!function(e){"function"!=typeof e.Promise&&(e.Promise=t(2))}.call(this,void 0!==r?r:"undefined"!=typeof self?self:"undefined"!=typeof window?window:{})},{2:2}],4:[function(e,r,F){var P="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},c=function(){try{return"undefined"!=typeof indexedDB?indexedDB:"undefined"!=typeof webkitIndexedDB?webkitIndexedDB:"undefined"!=typeof mozIndexedDB?mozIndexedDB:"undefined"!=typeof OIndexedDB?OIndexedDB:"undefined"!=typeof msIndexedDB?msIndexedDB:void 0}catch(e){}}();function f(t,n){t=t||[],n=n||{};try{return new Blob(t,n)}catch(e){if("TypeError"!==e.name)throw e;for(var r=new("undefined"!=typeof BlobBuilder?BlobBuilder:"undefined"!=typeof MSBlobBuilder?MSBlobBuilder:"undefined"!=typeof MozBlobBuilder?MozBlobBuilder:WebKitBlobBuilder),o=0;o<t.length;o+=1)r.append(t[o]);return r.getBlob(n.type)}}"undefined"==typeof Promise&&e(3);var h=Promise;function v(e,t){t&&e.then(function(e){t(null,e)},function(e){t(e)})}function o(e,t,n){"function"==typeof t&&e.then(t),"function"==typeof n&&e.catch(n)}function s(e){return"string"!=typeof e&&(console.warn(e+" used as a key, but it is not a string."),e=String(e)),e}function i(){if(arguments.length&&"function"==typeof arguments[arguments.length-1])return arguments[arguments.length-1]}var l=void 0,d={},M=Object.prototype.toString;function u(e){var e=d[e.name],n={};n.promise=new h(function(e,t){n.resolve=e,n.reject=t}),e.deferredOperations.push(n),e.dbReady?e.dbReady=e.dbReady.then(function(){return n.promise}):e.dbReady=n.promise}function p(e){e=d[e.name].deferredOperations.pop();e&&(e.resolve(),e.promise)}function y(e,t){e=d[e.name].deferredOperations.pop();if(e)return e.reject(t),e.promise}function t(o,i){return new h(function(t,n){if(d[o.name]=d[o.name]||{forages:[],db:null,dbReady:null,deferredOperations:[]},o.db){if(!i)return t(o.db);u(o),o.db.close()}var e=[o.name],r=(i&&e.push(o.version),c.open.apply(c,e));i&&(r.onupgradeneeded=function(e){var t=r.result;try{t.createObjectStore(o.storeName),e.oldVersion<=1&&t.createObjectStore("local-forage-detect-blob-support")}catch(t){if("ConstraintError"!==t.name)throw t;console.warn('The database "'+o.name+'" has been upgraded from version '+e.oldVersion+" to version "+e.newVersion+', but the storage "'+o.storeName+'" already exists.')}}),r.onerror=function(e){e.preventDefault(),n(r.error)},r.onsuccess=function(){var e=r.result;e.onversionchange=function(e){e.target.close()},t(e),p(o)}})}function b(e){return t(e,!1)}function m(e){return t(e,!0)}function g(e,t){var n,r,o;return!e.db||(n=!e.db.objectStoreNames.contains(e.storeName),o=e.version<e.db.version,r=e.version>e.db.version,o&&(e.version!==t&&console.warn('The database "'+e.name+"\" can't be downgraded from version "+e.db.version+" to version "+e.version+"."),e.version=e.db.version),(r||n)&&(n&&(o=e.db.version+1)>e.version&&(e.version=o),1))}function _(e){return f([function(e){for(var t=e.length,n=new ArrayBuffer(t),r=new Uint8Array(n),o=0;o<t;o++)r[o]=e.charCodeAt(o);return n}(atob(e.data))],{type:e.type})}function w(e){return e&&e.__local_forage_encoded_blob}function z(e){var t=this,n=t._initReady().then(function(){var e=d[t._dbInfo.name];if(e&&e.dbReady)return e.dbReady});return o(n,e,e),n}function I(e,t,n,r){void 0===r&&(r=1);try{var o=e.db.transaction(e.storeName,t);n(null,o)}catch(o){if(0<r&&(!e.db||"InvalidStateError"===o.name||"NotFoundError"===o.name))return h.resolve().then(function(){if(!e.db||"NotFoundError"===o.name&&!e.db.objectStoreNames.contains(e.storeName)&&e.version<=e.db.version)return e.db&&(e.version=e.db.version+1),m(e)}).then(function(){return function(n){u(n);for(var r=d[n.name],o=r.forages,e=0;e<o.length;e++){var t=o[e];t._dbInfo.db&&(t._dbInfo.db.close(),t._dbInfo.db=null)}return n.db=null,b(n).then(function(e){return n.db=e,g(n)?m(n):e}).then(function(e){n.db=r.db=e;for(var t=0;t<o.length;t++)o[t]._dbInfo.db=e}).catch(function(e){throw y(n,e),e})}(e).then(function(){I(e,t,n,r-1)})}).catch(n);n(o)}}var e={_driver:"asyncStorage",_initStorage:function(e){var r=this,o={db:null};if(e)for(var t in e)o[t]=e[t];var i=d[o.name],n=(i||(i={forages:[],db:null,dbReady:null,deferredOperations:[]},d[o.name]=i),i.forages.push(r),r._initReady||(r._initReady=r.ready,r.ready=z),[]);function a(){return h.resolve()}for(var c=0;c<i.forages.length;c++){var u=i.forages[c];u!==r&&n.push(u._initReady().catch(a))}var f=i.forages.slice(0);return h.all(n).then(function(){return o.db=i.db,b(o)}).then(function(e){return o.db=e,g(o,r._defaultConfig.version)?m(o):e}).then(function(e){o.db=i.db=e,r._dbInfo=o;for(var t=0;t<f.length;t++){var n=f[t];n!==r&&(n._dbInfo.db=o.db,n._dbInfo.version=o.version)}})},_support:function(){try{var e,t;return c&&c.open?(e="undefined"!=typeof openDatabase&&/(Safari|iPhone|iPad|iPod)/.test(navigator.userAgent)&&!/Chrome/.test(navigator.userAgent)&&!/BlackBerry/.test(navigator.platform),t="function"==typeof fetch&&-1!==fetch.toString().indexOf("[native code"),(!e||t)&&"undefined"!=typeof indexedDB&&"undefined"!=typeof IDBKeyRange):!1}catch(e){return!1}}(),iterate:function(a,e){var c=this,t=new h(function(o,i){c.ready().then(function(){I(c._dbInfo,"readonly",function(e,t){if(e)return i(e);try{var n=t.objectStore(c._dbInfo.storeName).openCursor(),r=1;n.onsuccess=function(){var e,t=n.result;t?(w(e=t.value)&&(e=_(e)),void 0!==(e=a(e,t.key,r++))?o(e):t.continue()):o()},n.onerror=function(){i(n.error)}}catch(e){i(e)}})}).catch(i)});return v(t,e),t},getItem:function(i,e){var a=this,t=(i=s(i),new h(function(r,o){a.ready().then(function(){I(a._dbInfo,"readonly",function(e,t){if(e)return o(e);try{var n=t.objectStore(a._dbInfo.storeName).get(i);n.onsuccess=function(){var e=n.result;w(e=void 0===e?null:e)&&(e=_(e)),r(e)},n.onerror=function(){o(n.error)}}catch(e){o(e)}})}).catch(o)}));return v(t,e),t},setItem:function(c,n,e){var u=this,t=(c=s(c),new h(function(i,a){var t;u.ready().then(function(){return t=u._dbInfo,"[object Blob]"===M.call(n)?(e=t.db,("boolean"==typeof l?h.resolve(l):(r=e,new h(function(n){var e=r.transaction("local-forage-detect-blob-support","readwrite"),t=f([""]);e.objectStore("local-forage-detect-blob-support").put(t,"key"),e.onabort=function(e){e.preventDefault(),e.stopPropagation(),n(!1)},e.oncomplete=function(){var e=navigator.userAgent.match(/Chrome\/(\d+)/),t=navigator.userAgent.match(/Edge\//);n(t||!e||43<=parseInt(e[1],10))}}).catch(function(){return!1}).then(function(e){return l=e}))).then(function(e){return e?n:(r=n,new h(function(t,e){var n=new FileReader;n.onerror=e,n.onloadend=function(e){e=btoa(e.target.result||"");t({__local_forage_encoded_blob:!0,data:e,type:r.type})},n.readAsBinaryString(r)}));var r})):n;var e,r}).then(function(o){I(u._dbInfo,"readwrite",function(e,t){if(e)return a(e);try{var n=t.objectStore(u._dbInfo.storeName),r=(null===o&&(o=void 0),n.put(o,c));t.oncomplete=function(){i(o=void 0===o?null:o)},t.onabort=t.onerror=function(){var e=r.error||r.transaction.error;a(e)}}catch(e){a(e)}})}).catch(a)}));return v(t,e),t},removeItem:function(i,e){var a=this,t=(i=s(i),new h(function(r,o){a.ready().then(function(){I(a._dbInfo,"readwrite",function(e,t){if(e)return o(e);try{var n=t.objectStore(a._dbInfo.storeName).delete(i);t.oncomplete=function(){r()},t.onerror=function(){o(n.error)},t.onabort=function(){var e=n.error||n.transaction.error;o(e)}}catch(e){o(e)}})}).catch(o)}));return v(t,e),t},clear:function(e){var i=this,t=new h(function(r,o){i.ready().then(function(){I(i._dbInfo,"readwrite",function(e,t){if(e)return o(e);try{var n=t.objectStore(i._dbInfo.storeName).clear();t.oncomplete=function(){r()},t.onabort=t.onerror=function(){var e=n.error||n.transaction.error;o(e)}}catch(e){o(e)}})}).catch(o)});return v(t,e),t},length:function(e){var i=this,t=new h(function(r,o){i.ready().then(function(){I(i._dbInfo,"readonly",function(e,t){if(e)return o(e);try{var n=t.objectStore(i._dbInfo.storeName).count();n.onsuccess=function(){r(n.result)},n.onerror=function(){o(n.error)}}catch(e){o(e)}})}).catch(o)});return v(t,e),t},key:function(c,e){var u=this,t=new h(function(i,a){c<0?i(null):u.ready().then(function(){I(u._dbInfo,"readonly",function(e,t){if(e)return a(e);try{var n=t.objectStore(u._dbInfo.storeName),r=!1,o=n.openKeyCursor();o.onsuccess=function(){var e=o.result;e?0===c||r?i(e.key):(r=!0,e.advance(c)):i(null)},o.onerror=function(){a(o.error)}}catch(e){a(e)}})}).catch(a)});return v(t,e),t},keys:function(e){var a=this,t=new h(function(o,i){a.ready().then(function(){I(a._dbInfo,"readonly",function(e,t){if(e)return i(e);try{var n=t.objectStore(a._dbInfo.storeName).openKeyCursor(),r=[];n.onsuccess=function(){var e=n.result;e?(r.push(e.key),e.continue()):o(r)},n.onerror=function(){i(n.error)}}catch(e){i(e)}})}).catch(i)});return v(t,e),t},dropInstance:function(a,e){e=i.apply(this,arguments);var t=this.config();(a="function"!=typeof a&&a||{}).name||(a.name=a.name||t.name,a.storeName=a.storeName||t.storeName);return v(t=a.name?(t=a.name===t.name&&this._dbInfo.db?h.resolve(this._dbInfo.db):b(a).then(function(e){var t=d[a.name],n=t.forages;t.db=e;for(var r=0;r<n.length;r++)n[r]._dbInfo.db=e;return e}),a.storeName?t.then(function(e){if(e.objectStoreNames.contains(a.storeName)){var o=e.version+1,r=(u(a),d[a.name]),i=r.forages;e.close();for(var t=0;t<i.length;t++){var n=i[t];n._dbInfo.db=null,n._dbInfo.version=o}return new h(function(t,n){var r=c.open(a.name,o);r.onerror=function(e){r.result.close(),n(e)},r.onupgradeneeded=function(){r.result.deleteObjectStore(a.storeName)},r.onsuccess=function(){var e=r.result;e.close(),t(e)}}).then(function(e){r.db=e;for(var t=0;t<i.length;t++){var n=i[t];n._dbInfo.db=e,p(n._dbInfo)}}).catch(function(e){throw(y(a,e)||h.resolve()).catch(function(){}),e})}}):t.then(function(e){u(a);var n=d[a.name],r=n.forages;e.close();for(var t=0;t<r.length;t++)r[t]._dbInfo.db=null;return new h(function(t,n){var r=c.deleteDatabase(a.name);r.onerror=function(){var e=r.result;e&&e.close(),n(r.error)},r.onblocked=function(){console.warn('dropInstance blocked for database "'+a.name+'" until all open connections are closed')},r.onsuccess=function(){var e=r.result;e&&e.close(),t(e)}}).then(function(e){n.db=e;for(var t=0;t<r.length;t++)p(r[t]._dbInfo)}).catch(function(e){throw(y(a,e)||h.resolve()).catch(function(){}),e})})):h.reject("Invalid arguments"),e),t}},S="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",a=/^~~local_forage_type~([^~]+)~/,E="__lfsc__:".length,N=E+"arbf".length,j=Object.prototype.toString;function x(e){for(var t,n,r,o,i=.75*e.length,a=e.length,c=0,i=("="===e[e.length-1]&&(i--,"="===e[e.length-2])&&i--,new ArrayBuffer(i)),u=new Uint8Array(i),f=0;f<a;f+=4)t=S.indexOf(e[f]),n=S.indexOf(e[f+1]),r=S.indexOf(e[f+2]),o=S.indexOf(e[f+3]),u[c++]=t<<2|n>>4,u[c++]=(15&n)<<4|r>>2,u[c++]=(3&r)<<6|63&o;return i}function O(e){for(var t=new Uint8Array(e),n="",r=0;r<t.length;r+=3)n=(n=(n=(n+=S[t[r]>>2])+S[(3&t[r])<<4|t[r+1]>>4])+S[(15&t[r+1])<<2|t[r+2]>>6])+S[63&t[r+2]];return t.length%3==2?n=n.substring(0,n.length-1)+"=":t.length%3==1&&(n=n.substring(0,n.length-2)+"=="),n}var k={serialize:function(t,n){var e="";if(t&&(e=j.call(t)),t&&("[object ArrayBuffer]"===e||t.buffer&&"[object ArrayBuffer]"===j.call(t.buffer))){var r,o="__lfsc__:";t instanceof ArrayBuffer?(r=t,o+="arbf"):(r=t.buffer,"[object Int8Array]"===e?o+="si08":"[object Uint8Array]"===e?o+="ui08":"[object Uint8ClampedArray]"===e?o+="uic8":"[object Int16Array]"===e?o+="si16":"[object Uint16Array]"===e?o+="ur16":"[object Int32Array]"===e?o+="si32":"[object Uint32Array]"===e?o+="ui32":"[object Float32Array]"===e?o+="fl32":"[object Float64Array]"===e?o+="fl64":n(new Error("Failed to get type for BinaryArray"))),n(o+O(r))}else if("[object Blob]"===e){o=new FileReader;o.onload=function(){var e="~~local_forage_type~"+t.type+"~"+O(this.result);n("__lfsc__:blob"+e)},o.readAsArrayBuffer(t)}else try{n(JSON.stringify(t))}catch(e){console.error("Couldn't convert value into a JSON string: ",t),n(null,e)}},deserialize:function(e){if("__lfsc__:"!==e.substring(0,E))return JSON.parse(e);var t,n=e.substring(N),r=e.substring(E,N),o=("blob"===r&&a.test(n)&&(t=(e=n.match(a))[1],n=n.substring(e[0].length)),x(n));switch(r){case"arbf":return o;case"blob":return f([o],{type:t});case"si08":return new Int8Array(o);case"ui08":return new Uint8Array(o);case"uic8":return new Uint8ClampedArray(o);case"si16":return new Int16Array(o);case"ur16":return new Uint16Array(o);case"si32":return new Int32Array(o);case"ui32":return new Uint32Array(o);case"fl32":return new Float32Array(o);case"fl64":return new Float64Array(o);default:throw new Error("Unkown type: "+r)}},stringToBuffer:x,bufferToString:O};function U(e,t,n,r){e.executeSql("CREATE TABLE IF NOT EXISTS "+t.storeName+" (id INTEGER PRIMARY KEY, key unique, value)",[],n,r)}function A(e,r,o,i,a,c){e.executeSql(o,i,a,function(e,n){n.code===n.SYNTAX_ERR?e.executeSql("SELECT name FROM sqlite_master WHERE type='table' AND name = ?",[r.storeName],function(e,t){t.rows.length?c(e,n):U(e,r,function(){e.executeSql(o,i,a,c)},c)},c):c(e,n)},c)}function q(a,e,c,u){var f=this,t=(a=s(a),new h(function(o,i){f.ready().then(function(){var n=e=void 0===e?null:e,r=f._dbInfo;r.serializer.serialize(e,function(t,e){e?i(e):r.db.transaction(function(e){A(e,r,"INSERT OR REPLACE INTO "+r.storeName+" (key, value) VALUES (?, ?)",[a,t],function(){o(n)},function(e,t){i(t)})},function(e){e.code===e.QUOTA_ERR&&(0<u?o(q.apply(f,[a,n,c,u-1])):i(e))})})}).catch(i)}));return v(t,c),t}var n={_driver:"webSQLStorage",_initStorage:function(e){var r=this,o={db:null};if(e)for(var t in e)o[t]="string"!=typeof e[t]?e[t].toString():e[t];var n=new h(function(t,n){try{o.db=openDatabase(o.name,String(o.version),o.description,o.size)}catch(t){return n(t)}o.db.transaction(function(e){U(e,o,function(){r._dbInfo=o,t()},function(e,t){n(t)})},n)});return o.serializer=k,n},_support:"function"==typeof openDatabase,iterate:function(f,e){var t=this,n=new h(function(u,n){t.ready().then(function(){var c=t._dbInfo;c.db.transaction(function(e){A(e,c,"SELECT * FROM "+c.storeName,[],function(e,t){for(var n=t.rows,r=n.length,o=0;o<r;o++){var i=n.item(o),a=(a=i.value)&&c.serializer.deserialize(a);if(void 0!==(a=f(a,i.key,o+1)))return void u(a)}u()},function(e,t){n(t)})})}).catch(n)});return v(n,e),n},getItem:function(t,e){var i=this,n=(t=s(t),new h(function(r,o){i.ready().then(function(){var n=i._dbInfo;n.db.transaction(function(e){A(e,n,"SELECT * FROM "+n.storeName+" WHERE key = ? LIMIT 1",[t],function(e,t){t=(t=t.rows.length?t.rows.item(0).value:null)&&n.serializer.deserialize(t);r(t)},function(e,t){o(t)})})}).catch(o)}));return v(n,e),n},setItem:function(e,t,n){return q.apply(this,[e,t,n,1])},removeItem:function(o,e){var i=this,t=(o=s(o),new h(function(n,r){i.ready().then(function(){var t=i._dbInfo;t.db.transaction(function(e){A(e,t,"DELETE FROM "+t.storeName+" WHERE key = ?",[o],function(){n()},function(e,t){r(t)})})}).catch(r)}));return v(t,e),t},clear:function(e){var o=this,t=new h(function(n,r){o.ready().then(function(){var t=o._dbInfo;t.db.transaction(function(e){A(e,t,"DELETE FROM "+t.storeName,[],function(){n()},function(e,t){r(t)})})}).catch(r)});return v(t,e),t},length:function(e){var o=this,t=new h(function(n,r){o.ready().then(function(){var t=o._dbInfo;t.db.transaction(function(e){A(e,t,"SELECT COUNT(key) as c FROM "+t.storeName,[],function(e,t){t=t.rows.item(0).c;n(t)},function(e,t){r(t)})})}).catch(r)});return v(t,e),t},key:function(o,e){var i=this,t=new h(function(n,r){i.ready().then(function(){var t=i._dbInfo;t.db.transaction(function(e){A(e,t,"SELECT key FROM "+t.storeName+" WHERE id = ? LIMIT 1",[o+1],function(e,t){t=t.rows.length?t.rows.item(0).key:null;n(t)},function(e,t){r(t)})})}).catch(r)});return v(t,e),t},keys:function(e){var r=this,t=new h(function(o,n){r.ready().then(function(){var t=r._dbInfo;t.db.transaction(function(e){A(e,t,"SELECT key FROM "+t.storeName,[],function(e,t){for(var n=[],r=0;r<t.rows.length;r++)n.push(t.rows.item(r).key);o(n)},function(e,t){n(t)})})}).catch(n)});return v(t,e),t},dropInstance:function(n,e){e=i.apply(this,arguments);var r=this.config();(n="function"!=typeof n&&n||{}).name||(n.name=n.name||r.name,n.storeName=n.storeName||r.storeName);var t,o=this;return v(t=n.name?new h(function(e){var i,t=n.name===r.name?o._dbInfo.db:openDatabase(n.name,"","",0);n.storeName?e({db:t,storeNames:[n.storeName]}):e((i=t,new h(function(o,n){i.transaction(function(e){e.executeSql("SELECT name FROM sqlite_master WHERE type='table' AND name <> '__WebKitDatabaseInfoTable__'",[],function(e,t){for(var n=[],r=0;r<t.rows.length;r++)n.push(t.rows.item(r).name);o({db:i,storeNames:n})},function(e,t){n(t)})},function(e){n(e)})})))}).then(function(a){return new h(function(o,i){a.db.transaction(function(r){for(var e=[],t=0,n=a.storeNames.length;t<n;t++)e.push(function(t){return new h(function(e,n){r.executeSql("DROP TABLE IF EXISTS "+t,[],function(){e()},function(e,t){n(t)})})}(a.storeNames[t]));h.all(e).then(function(){o()}).catch(function(e){i(e)})},function(e){i(e)})})}):h.reject("Invalid arguments"),e),t}};function W(e,t){var n=e.name+"/";return e.storeName!==t.storeName&&(n+=e.storeName+"/"),n}var G={_driver:"localStorageWrapper",_initStorage:function(e){var t={};if(e)for(var n in e)t[n]=e[n];return t.keyPrefix=W(e,this._defaultConfig),!function(){try{return localStorage.setItem("_localforage_support_test",!0),localStorage.removeItem("_localforage_support_test"),0}catch(e){return 1}}()||0<localStorage.length?((this._dbInfo=t).serializer=k,h.resolve()):h.reject()},_support:function(){try{return"undefined"!=typeof localStorage&&"setItem"in localStorage&&!!localStorage.setItem}catch(e){return!1}}(),iterate:function(u,e){var f=this,t=f.ready().then(function(){for(var e=f._dbInfo,t=e.keyPrefix,n=t.length,r=localStorage.length,o=1,i=0;i<r;i++){var a=localStorage.key(i);if(0===a.indexOf(t)){var c=(c=localStorage.getItem(a))&&e.serializer.deserialize(c);if(void 0!==(c=u(c,a.substring(n),o++)))return c}}});return v(t,e),t},getItem:function(n,e){var r=this,t=(n=s(n),r.ready().then(function(){var e=r._dbInfo,t=localStorage.getItem(e.keyPrefix+n);return t=t&&e.serializer.deserialize(t)}));return v(t,e),t},setItem:function(a,e,t){var c=this,n=(a=s(a),c.ready().then(function(){var i=e=void 0===e?null:e;return new h(function(n,r){var o=c._dbInfo;o.serializer.serialize(e,function(e,t){if(t)r(t);else try{localStorage.setItem(o.keyPrefix+a,e),n(i)}catch(e){"QuotaExceededError"!==e.name&&"NS_ERROR_DOM_QUOTA_REACHED"!==e.name||r(e),r(e)}})})}));return v(n,t),n},removeItem:function(t,e){var n=this,r=(t=s(t),n.ready().then(function(){var e=n._dbInfo;localStorage.removeItem(e.keyPrefix+t)}));return v(r,e),r},clear:function(e){var r=this,t=r.ready().then(function(){for(var e=r._dbInfo.keyPrefix,t=localStorage.length-1;0<=t;t--){var n=localStorage.key(t);0===n.indexOf(e)&&localStorage.removeItem(n)}});return v(t,e),t},length:function(e){var t=this.keys().then(function(e){return e.length});return v(t,e),t},key:function(n,e){var r=this,t=r.ready().then(function(){var t,e=r._dbInfo;try{t=localStorage.key(n)}catch(e){t=null}return t=t&&t.substring(e.keyPrefix.length)});return v(t,e),t},keys:function(e){var i=this,t=i.ready().then(function(){for(var e=i._dbInfo,t=localStorage.length,n=[],r=0;r<t;r++){var o=localStorage.key(r);0===o.indexOf(e.keyPrefix)&&n.push(o.substring(e.keyPrefix.length))}return n});return v(t,e),t},dropInstance:function(t,e){e=i.apply(this,arguments),(t="function"!=typeof t&&t||{}).name||(n=this.config(),t.name=t.name||n.name,t.storeName=t.storeName||n.storeName);var n,r=this;return v(n=t.name?new h(function(e){t.storeName?e(W(t,r._defaultConfig)):e(t.name+"/")}).then(function(e){for(var t=localStorage.length-1;0<=t;t--){var n=localStorage.key(t);0===n.indexOf(e)&&localStorage.removeItem(n)}}):h.reject("Invalid arguments"),e),n}},J=Array.isArray||function(e){return"[object Array]"===Object.prototype.toString.call(e)},R={},K={},L={INDEXEDDB:e,WEBSQL:n,LOCALSTORAGE:G},e=[L.INDEXEDDB._driver,L.WEBSQL._driver,L.LOCALSTORAGE._driver],D=["dropInstance"],T=["clear","getItem","iterate","key","keys","length","removeItem","setItem"].concat(D),H={description:"",driver:e.slice(),name:"localforage",size:4980736,storeName:"keyvaluepairs",version:1};function B(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];if(n)for(var r in n)n.hasOwnProperty(r)&&(J(n[r])?e[r]=n[r].slice():e[r]=n[r])}return e}C.prototype.config=function(e){if("object"!==(void 0===e?"undefined":P(e)))return"string"==typeof e?this._config[e]:this._config;if(this._ready)return new Error("Can't call config() after localforage has been used.");for(var t in e){if("storeName"===t&&(e[t]=e[t].replace(/\W/g,"_")),"version"===t&&"number"!=typeof e[t])return new Error("Database version must be a number.");this._config[t]=e[t]}return!("driver"in e)||!e.driver||this.setDriver(this._config.driver)},C.prototype.defineDriver=function(d,e,t){var n=new h(function(t,n){try{var r=d._driver,e=new Error("Custom driver not compliant; see https://mozilla.github.io/localForage/#definedriver");if(d._driver){for(var o=T.concat("_initStorage"),i=0,a=o.length;i<a;i++){var c=o[i];if((!function(e,t){for(var n,r,o=e.length,i=0;i<o;){if((n=e[i])===(r=t)||"number"==typeof n&&"number"==typeof r&&isNaN(n)&&isNaN(r))return!0;i++}return!1}(D,c)||d[c])&&"function"!=typeof d[c])return void n(e)}for(var u=0,f=D.length;u<f;u++){var s=D[u];d[s]||(d[s]=function(t){return function(){var e=new Error("Method "+t+" is not implemented by the current driver"),e=h.reject(e);return v(e,arguments[arguments.length-1]),e}}(s))}var l=function(e){R[r]&&console.info("Redefining LocalForage driver: "+r),R[r]=d,K[r]=e,t()};"_support"in d?d._support&&"function"==typeof d._support?d._support().then(l,n):l(!!d._support):l(!0)}else n(e)}catch(e){n(e)}});return o(n,e,t),n},C.prototype.driver=function(){return this._driver||null},C.prototype.getDriver=function(e,t,n){e=R[e]?h.resolve(R[e]):h.reject(new Error("Driver not found."));return o(e,t,n),e},C.prototype.getSerializer=function(e){var t=h.resolve(k);return o(t,e),t},C.prototype.ready=function(e){var t=this,n=t._driverSet.then(function(){return null===t._ready&&(t._ready=t._initDriver()),t._ready});return o(n,e,e),n},C.prototype.setDriver=function(e,t,n){var i=this,r=(J(e)||(e=[e]),this._getSupportedDrivers(e));function a(){i._config.driver=i.driver()}function c(e){return i._extend(e),a(),i._ready=i._initStorage(i._config),i._ready}e=null!==this._driverSet?this._driverSet.catch(function(){return h.resolve()}):h.resolve();return this._driverSet=e.then(function(){var e=r[0];return i._dbInfo=null,i._ready=null,i.getDriver(e).then(function(e){var o;i._driver=e._driver,a(),i._wrapLibraryMethodsWithReady(),i._initDriver=(o=r,function(){var r=0;return function e(){for(;r<o.length;){var t=o[r];return r++,i._dbInfo=null,i._ready=null,i.getDriver(t).then(c).catch(e)}a();var n=new Error("No available storage method found.");return i._driverSet=h.reject(n),i._driverSet}()})})}).catch(function(){a();var e=new Error("No available storage method found.");return i._driverSet=h.reject(e),i._driverSet}),o(this._driverSet,t,n),this._driverSet},C.prototype.supports=function(e){return!!K[e]},C.prototype._extend=function(e){B(this,e)},C.prototype._getSupportedDrivers=function(e){for(var t=[],n=0,r=e.length;n<r;n++){var o=e[n];this.supports(o)&&t.push(o)}return t},C.prototype._wrapLibraryMethodsWithReady=function(){for(var e=0,t=T.length;e<t;e++)!function(t,n){t[n]=function(){var e=arguments;return t.ready().then(function(){return t[n].apply(t,e)})}}(this,T[e])},C.prototype.createInstance=function(e){return new C(e)};n=new C;function C(e){var t,n,r;if(!(this instanceof C))throw new TypeError("Cannot call a class as a function");for(t in L)L.hasOwnProperty(t)&&(r=(n=L[t])._driver,this[t]=r,R[r]||this.defineDriver(n));this._defaultConfig=B({},H),this._config=B({},this._defaultConfig,e),this._driverSet=null,this._initDriver=null,this._ready=!1,this._dbInfo=null,this._wrapLibraryMethodsWithReady(),this.setDriver(this._config.driver).catch(function(){})}r.exports=n},{3:3}]},{},[4])(4)}.call(this,n(32))}}]);