(window.webpackJsonpfeffery_utils_components=window.webpackJsonpfeffery_utils_components||[]).push([[10],{548:function(e,t,r){r.r(t);var i=r(2),l=r(1),u=r(8),c=r(909),r=r(233);function T(e){return(T="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function k(){k=function(){return l};var u,l={},e=Object.prototype,c=e.hasOwnProperty,s=Object.defineProperty||function(e,t,r){e[t]=r.value},t="function"==typeof Symbol?Symbol:{},n=t.iterator||"@@iterator",r=t.asyncIterator||"@@asyncIterator",o=t.toStringTag||"@@toStringTag";function i(e,t,r){return Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}),e[t]}try{i({},"")}catch(u){i=function(e,t,r){return e[t]=r}}function a(e,t,r,n){var o,i,l,a,t=t&&t.prototype instanceof p?t:p,t=Object.create(t.prototype),n=new C(n||[]);return s(t,"_invoke",{value:(o=e,i=r,l=n,a=f,function(e,t){if(a===h)throw Error("Generator is already running");if(a===m){if("throw"===e)throw t;return{value:u,done:!0}}for(l.method=e,l.arg=t;;){var r=l.delegate;if(r){r=function e(t,r){var n=r.method,o=t.iterator[n];if(o===u)return r.delegate=null,"throw"===n&&t.iterator.return&&(r.method="return",r.arg=u,e(t,r),"throw"===r.method)||"return"!==n&&(r.method="throw",r.arg=new TypeError("The iterator does not provide a '"+n+"' method")),g;n=d(o,t.iterator,r.arg);if("throw"===n.type)return r.method="throw",r.arg=n.arg,r.delegate=null,g;o=n.arg;return o?o.done?(r[t.resultName]=o.value,r.next=t.nextLoc,"return"!==r.method&&(r.method="next",r.arg=u),r.delegate=null,g):o:(r.method="throw",r.arg=new TypeError("iterator result is not an object"),r.delegate=null,g)}(r,l);if(r){if(r===g)continue;return r}}if("next"===l.method)l.sent=l._sent=l.arg;else if("throw"===l.method){if(a===f)throw a=m,l.arg;l.dispatchException(l.arg)}else"return"===l.method&&l.abrupt("return",l.arg);a=h;r=d(o,i,l);if("normal"===r.type){if(a=l.done?m:"suspendedYield",r.arg===g)continue;return{value:r.arg,done:l.done}}"throw"===r.type&&(a=m,l.method="throw",l.arg=r.arg)}})}),t}function d(e,t,r){try{return{type:"normal",arg:e.call(t,r)}}catch(e){return{type:"throw",arg:e}}}l.wrap=a;var f="suspendedStart",h="executing",m="completed",g={};function p(){}function y(){}function w(){}var t={},v=(i(t,n,function(){return this}),Object.getPrototypeOf),v=v&&v(v(N([]))),b=(v&&v!==e&&c.call(v,n)&&(t=v),w.prototype=p.prototype=Object.create(t));function S(e){["next","throw","return"].forEach(function(t){i(e,t,function(e){return this._invoke(t,e)})})}function E(l,a){var t;s(this,"_invoke",{value:function(r,n){function e(){return new a(function(e,t){!function t(e,r,n,o){var i,e=d(l[e],l,r);if("throw"!==e.type)return(r=(i=e.arg).value)&&"object"==T(r)&&c.call(r,"__await")?a.resolve(r.__await).then(function(e){t("next",e,n,o)},function(e){t("throw",e,n,o)}):a.resolve(r).then(function(e){i.value=e,n(i)},function(e){return t("throw",e,n,o)});o(e.arg)}(r,n,e,t)})}return t=t?t.then(e,e):e()}})}function x(e){var t={tryLoc:e[0]};1 in e&&(t.catchLoc=e[1]),2 in e&&(t.finallyLoc=e[2],t.afterLoc=e[3]),this.tryEntries.push(t)}function A(e){var t=e.completion||{};t.type="normal",delete t.arg,e.completion=t}function C(e){this.tryEntries=[{tryLoc:"root"}],e.forEach(x,this),this.reset(!0)}function N(t){if(t||""===t){var r,e=t[n];if(e)return e.call(t);if("function"==typeof t.next)return t;if(!isNaN(t.length))return r=-1,(e=function e(){for(;++r<t.length;)if(c.call(t,r))return e.value=t[r],e.done=!1,e;return e.value=u,e.done=!0,e}).next=e}throw new TypeError(T(t)+" is not iterable")}return s(b,"constructor",{value:y.prototype=w,configurable:!0}),s(w,"constructor",{value:y,configurable:!0}),y.displayName=i(w,o,"GeneratorFunction"),l.isGeneratorFunction=function(e){e="function"==typeof e&&e.constructor;return!!e&&(e===y||"GeneratorFunction"===(e.displayName||e.name))},l.mark=function(e){return Object.setPrototypeOf?Object.setPrototypeOf(e,w):(e.__proto__=w,i(e,o,"GeneratorFunction")),e.prototype=Object.create(b),e},l.awrap=function(e){return{__await:e}},S(E.prototype),i(E.prototype,r,function(){return this}),l.AsyncIterator=E,l.async=function(e,t,r,n,o){void 0===o&&(o=Promise);var i=new E(a(e,t,r,n),o);return l.isGeneratorFunction(t)?i:i.next().then(function(e){return e.done?e.value:i.next()})},S(b),i(b,o,"Generator"),i(b,n,function(){return this}),i(b,"toString",function(){return"[object Generator]"}),l.keys=function(e){var t,r=Object(e),n=[];for(t in r)n.push(t);return n.reverse(),function e(){for(;n.length;){var t=n.pop();if(t in r)return e.value=t,e.done=!1,e}return e.done=!0,e}},l.values=N,C.prototype={constructor:C,reset:function(e){if(this.prev=0,this.next=0,this.sent=this._sent=u,this.done=!1,this.delegate=null,this.method="next",this.arg=u,this.tryEntries.forEach(A),!e)for(var t in this)"t"===t.charAt(0)&&c.call(this,t)&&!isNaN(+t.slice(1))&&(this[t]=u)},stop:function(){this.done=!0;var e=this.tryEntries[0].completion;if("throw"===e.type)throw e.arg;return this.rval},dispatchException:function(r){if(this.done)throw r;var n=this;function e(e,t){return i.type="throw",i.arg=r,n.next=e,t&&(n.method="next",n.arg=u),!!t}for(var t=this.tryEntries.length-1;0<=t;--t){var o=this.tryEntries[t],i=o.completion;if("root"===o.tryLoc)return e("end");if(o.tryLoc<=this.prev){var l=c.call(o,"catchLoc"),a=c.call(o,"finallyLoc");if(l&&a){if(this.prev<o.catchLoc)return e(o.catchLoc,!0);if(this.prev<o.finallyLoc)return e(o.finallyLoc)}else if(l){if(this.prev<o.catchLoc)return e(o.catchLoc,!0)}else{if(!a)throw Error("try statement without catch or finally");if(this.prev<o.finallyLoc)return e(o.finallyLoc)}}}},abrupt:function(e,t){for(var r=this.tryEntries.length-1;0<=r;--r){var n=this.tryEntries[r];if(n.tryLoc<=this.prev&&c.call(n,"finallyLoc")&&this.prev<n.finallyLoc){var o=n;break}}var i=(o=o&&("break"===e||"continue"===e)&&o.tryLoc<=t&&t<=o.finallyLoc?null:o)?o.completion:{};return i.type=e,i.arg=t,o?(this.method="next",this.next=o.finallyLoc,g):this.complete(i)},complete:function(e,t){if("throw"===e.type)throw e.arg;return"break"===e.type||"continue"===e.type?this.next=e.arg:"return"===e.type?(this.rval=this.arg=e.arg,this.method="return",this.next="end"):"normal"===e.type&&t&&(this.next=t),g},finish:function(e){for(var t=this.tryEntries.length-1;0<=t;--t){var r=this.tryEntries[t];if(r.finallyLoc===e)return this.complete(r.completion,r.afterLoc),A(r),g}},catch:function(e){for(var t=this.tryEntries.length-1;0<=t;--t){var r,n,o=this.tryEntries[t];if(o.tryLoc===e)return"throw"===(r=o.completion).type&&(n=r.arg,A(o)),n}throw Error("illegal catch attempt")},delegateYield:function(e,t,r){return this.delegate={iterator:N(e),resultName:t,nextLoc:r},"next"===this.method&&(this.arg=u),g}},l}function s(e,t,r,n,o,i,l){try{var a=e[i](l),u=a.value}catch(e){return r(e)}a.done?t(u):Promise.resolve(u).then(n,o)}function n(e){var t,a,r=e.targetSelector,n=e.scale,o=e.setProps;return e.loading_state,a=k().mark(function e(){var t;return k().wrap(function(e){for(;;)switch(e.prev=e.next){case 0:r&&((t=document.querySelector(r))?Object(c.domToPng)(t,{scale:n}).then(function(e){o({screenshotResult:{selector:r,status:"success",dataUrl:e,timestamp:(new Date).getTime()}})}):o({screenshotResult:{selector:r,status:"failed",dataUrl:null,timestamp:(new Date).getTime()}}),o({targetSelector:null}));case 1:case"end":return e.stop()}},e)}),t=function(){var e=this,l=arguments;return new Promise(function(t,r){var n=a.apply(e,l);function o(e){s(n,t,r,o,i,"next",e)}function i(e){s(n,t,r,o,i,"throw",e)}o(void 0)})},e=[r],Object(l.useEffect)(function(){var r=t(),n=!1;return function(){Object(i.b)(this,void 0,void 0,function(){return Object(i.e)(this,function(e){switch(e.label){case 0:if(t=r,!Object(u.b)(t[Symbol.asyncIterator]))return[3,4];e.label=1;case 1:return[4,r.next()];case 2:return e.sent().done||n?[3,3]:[3,1];case 3:return[3,6];case 4:return[4,r];case 5:e.sent(),e.label=6;case 6:return[2]}var t})})}(),function(){n=!0}},e),React.createElement(React.Fragment,null)}(t.default=n).defaultProps=r.b,n.propTypes=r.c},909:function(e,t,o){{var r,Ee=Object.defineProperty,xe=Object.defineProperties,Ae=Object.getOwnPropertyDescriptors,$=Object.getOwnPropertySymbols,V=Object.prototype.hasOwnProperty,z=Object.prototype.propertyIsEnumerable,Ce=Math.pow,n=(e,t,r)=>t in e?Ee(e,t,{enumerable:!0,configurable:!0,writable:!0,value:r}):e[t]=r,G=(e,t)=>{for(var r in t=t||{})V.call(t,r)&&n(e,r,t[r]);if($)for(var r of $(t))z.call(t,r)&&n(e,r,t[r]);return e},H=(e,t)=>xe(e,Ae(t)),X=(e,l,a)=>new Promise((t,r)=>{var n=e=>{try{i(a.next(e))}catch(e){r(e)}},o=e=>{try{i(a.throw(e))}catch(e){r(e)}},i=e=>e.done?t(e.value):Promise.resolve(e.value).then(n,o);i((a=a.apply(e,l)).next())});function Y(e,t){return e[13]=1,e[14]=t>>8,e[15]=255&t,e[16]=t>>8,e[17]=255&t,e}let i="p".charCodeAt(0),l="H".charCodeAt(0),a="Y".charCodeAt(0),u="s".charCodeAt(0),c;function J(r,e,t=!1){var n=new Uint8Array(13),e=(e*=39.3701,n[0]=i,n[1]=l,n[2]=a,n[3]=u,n[4]=e>>>24,n[5]=e>>>16,n[6]=e>>>8,n[7]=255&e,n[8]=n[4],n[9]=n[5],n[10]=n[6],n[11]=n[7],n[12]=1,function(t){let r=-1;c=c||function(){var r=new Int32Array(256);for(let e=0;e<256;e++){let t=e;for(let e=0;e<8;e++)t=1&t?3988292384^t>>>1:t>>>1;r[e]=t}return r}();for(let e=0;e<t.length;e++)r=c[255&(r^t[e])]^r>>>8;return-1^r}(n)),o=new Uint8Array(4);if(o[0]=e>>>24,o[1]=e>>>16,o[2]=e>>>8,o[3]=255&e,t){let e=function(t){for(let e=t.length-1;4<=e;e--)if(9===t[e-4]&&t[e-3]===i&&t[e-2]===l&&t[e-1]===a&&t[e]===u)return e-3;return 0}(r);return r.set(n,e),r.set(o,e+13),r}{let e=new Uint8Array(4),t=(e[0]=0,e[1]=0,e[2]=0,e[3]=9,new Uint8Array(54));return t.set(r,0),t.set(e,33),t.set(n,37),t.set(o,50),t}}let v="[modern-screenshot]",b="undefined"!=typeof window,S=b&&"Worker"in window,f=b&&"atob"in window,h=b&&"btoa"in window,e=b?null==(r=window.navigator)?void 0:r.userAgent:"",E=e.includes("Chrome"),w=e.includes("AppleWebKit")&&!E,x=e.includes("Firefox"),A=e=>1===e.nodeType,C=e=>"object"==typeof e.className,N=e=>"image"===e.tagName,T=e=>A(e)&&void 0!==e.style&&!C(e),s=e=>8===e.nodeType,k=e=>"IMG"===e.tagName,D=e=>"VIDEO"===e.tagName,P=e=>"TEXTAREA"===e.tagName,d=e=>"SLOT"===e.tagName,L=(...e)=>console.warn(v,...e),O=e=>e.startsWith("data:");function K(e,t){var r,n,o;return e.match(/^[a-z]+:\/\//i)?e:b&&e.match(/^\/\//)?window.location.protocol+e:e.match(/^[a-z]+:/i)||!b?e:(n=(r=Q().implementation.createHTMLDocument()).createElement("base"),o=r.createElement("a"),r.head.appendChild(n),r.body.appendChild(o),t&&(n.href=t),o.href=e,o.href)}function Q(e){return null!=(e=e&&A(e)?null==e?void 0:e.ownerDocument:e)?e:window.document}let _="http://www.w3.org/2000/svg";function Z(e,t,r){r=Q(r).createElementNS(_,"svg");return r.setAttributeNS(null,"width",e.toString()),r.setAttributeNS(null,"height",t.toString()),r.setAttributeNS(null,"viewBox",`0 0 ${e} `+t),r}function ee(e,t){let r=(new XMLSerializer).serializeToString(e);return t&&(r=r.replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F\uD800-\uDFFF\uFFFE\uFFFF]/gu,"")),"data:image/svg+xml;charset=utf-8,"+encodeURIComponent(r)}function Ne(l,a="image/png",u=1){return X(this,null,function*(){try{return yield new Promise((t,r)=>{l.toBlob(e=>{e?t(e):r(new Error("Blob is null"))},a,u)})}catch(e){if(f){L("Failed canvas to blob",{type:a,quality:u},e);var[t,r]=l.toDataURL(a,u).split(","),t=null!=(t=null==(t=t.match(/data:(.+);/))?void 0:t[1])?t:void 0,n=window.atob(r),o=n.length,i=new Uint8Array(o);for(let e=0;e<o;e+=1)i[e]=n.charCodeAt(e);return new Blob([i],{type:t})}throw e}})}function te(n,o){return new Promise((e,t)=>{let r=new FileReader;r.onload=()=>e(r.result),r.onerror=()=>t(r.error),r.onabort=()=>t(new Error("Failed read blob to "+o)),"dataUrl"===o?r.readAsDataURL(n):"arrayBuffer"===o&&r.readAsArrayBuffer(n)})}let y=e=>te(e,"dataUrl");function re(e,t){t=Q(t).createElement("img");return t.decoding="sync",t.loading="eager",t.src=e,t}function ne(u,c){return new Promise(n=>{let{timeout:e,ownerDocument:t,onError:o}=null!=c?c:{},i="string"==typeof u?re(u,Q(t)):u,r=null,l=null;function a(){n(i),r&&clearTimeout(r),null!=l&&l()}if(e&&(r=setTimeout(a,e)),D(i)){let t=i.currentSrc||i.src;if(!t)return i.poster?ne(i.poster,c).then(n):a();if(2<=i.readyState)return a();let e=a,r=e=>{L("Failed video load",t,e),null!=o&&o(e),a()};l=()=>{i.removeEventListener("loadeddata",e),i.removeEventListener("error",r)},i.addEventListener("loadeddata",e,{once:!0}),i.addEventListener("error",r,{once:!0})}else{let t=N(i)?i.href.baseVal:i.currentSrc||i.src;if(!t)return a();let e=()=>X(this,null,function*(){if(k(i)&&"decode"in i)try{yield i.decode()}catch(e){L("Failed to decode image, trying to render anyway",i.dataset.originalSrc||t,e)}a()}),r=e=>{L("Failed image load",i.dataset.originalSrc||t,e),a()};if(k(i)&&i.complete)return e();l=()=>{i.removeEventListener("load",e),i.removeEventListener("error",r)},i.addEventListener("load",e,{once:!0}),i.addEventListener("error",r,{once:!0})}})}function oe(t,r){return X(this,null,function*(){T(t)&&(k(t)||D(t)?yield ne(t,{timeout:r}):yield Promise.all(["img","video"].flatMap(e=>Array.from(t.querySelectorAll(e)).map(e=>ne(e,{timeout:r})))))})}let F=function(){let e=0;return()=>(e+=1,"u"+("0000"+(Math.random()*Ce(36,4)<<0).toString(36)).slice(-4)+e)}();function ie(e){return null==e?void 0:e.split(",").map(e=>e.trim().replace(/"|'/g,"").toLowerCase()).filter(Boolean)}function le(e,t){return X(this,null,function*(){return e&&"__CONTEXT__"in e?e:ae(e,H(G({},t),{autoDestruct:!0}))})}function ae(y,w){return X(this,null,function*(){let e,t,r,n,o,{scale:i=1,workerUrl:l,workerNumber:a=1}=w||{},u=Boolean(null==w?void 0:w.debug),c=null==(e=null==w?void 0:w.features)||e,s=null!=(t=y.ownerDocument)?t:b?window.document:void 0,d=null!=(n=null==(r=y.ownerDocument)?void 0:r.defaultView)?n:b?window:void 0,f=new Map,h=H(G({width:0,height:0,quality:1,type:"image/png",scale:i,backgroundColor:null,style:null,filter:null,maximumCanvasSize:0,timeout:3e4,progress:null,debug:u,fetch:G({requestInit:{cache:(null==(o=null==w?void 0:w.fetch)?void 0:o.bypassingCache)?"no-cache":"force-cache"},placeholderImage:"data:image/png;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",bypassingCache:!1},null==w?void 0:w.fetch),fetchFn:null,font:{},drawImageInterval:100,workerUrl:null,workerNumber:a,onCloneNode:null,onEmbedNode:null,onCreateForeignObjectSvg:null,includeStyleProperties:null,autoDestruct:!1},w),{__CONTEXT__:!0,log:(m=u,{time:e=>{return m&&(e=e,console.time(v+" "+e))},timeEnd:e=>{return m&&(e=e,console.timeEnd(v+" "+e))},warn:(...e)=>m&&L(...e)}),node:y,ownerDocument:s,ownerWindow:d,dpi:1===i?null:96*i,svgStyleElement:ue(s),svgDefsElement:null==s?void 0:s.createElementNS(_,"defs"),svgStyles:new Map,defaultComputedStyles:new Map,workers:[...new Array(S&&l&&a?a:0)].map(()=>{try{var e=new Worker(l);return e.onmessage=o=>X(this,null,function*(){var e,t,{url:r,result:n}=o.data;n?null!=(e=null==(t=f.get(r))?void 0:t.resolve)&&e.call(t,n):null!=(t=null==(e=f.get(r))?void 0:e.reject)&&t.call(e,new Error("Error receiving message from worker: "+r))}),e.onmessageerror=e=>{var t,r,e=e.data["url"];null!=(r=null==(t=f.get(e))?void 0:t.reject)&&r.call(t,new Error("Error receiving message from worker: "+e))},e}catch(e){return L("Failed to new Worker",e),null}}).filter(Boolean),fontFamilies:new Set,fontCssTexts:new Map,acceptOfImage:[((p=null==(p=null==(g=s)?void 0:g.createElement)?void 0:p.call(g,"canvas"))&&(p.height=p.width=1),p&&"toDataURL"in p&&Boolean(p.toDataURL("image/webp").includes("image/webp"))&&"image/webp"),"image/svg+xml","image/*","*/*"].filter(Boolean).join(",")+";q=0.8",requests:f,drawImageCount:0,tasks:[],features:c,isEnable:e=>{var t;return"restoreScrollPosition"===e?"boolean"!=typeof c&&null!=(t=c[e])&&t:"boolean"==typeof c?c:null==(t=c[e])||t}});h.log.time("wait until load"),yield oe(y,h.timeout),h.log.timeEnd("wait until load");var m,{width:g,height:p}=function(t,e){let{width:r,height:n}=e;if(A(t)&&(!r||!n)){let e=t.getBoundingClientRect();r=r||e.width||Number(t.getAttribute("width"))||0,n=n||e.height||Number(t.getAttribute("height"))||0}return{width:r,height:n}}(y,h);return h.width=g,h.height=p,h})}function ue(e){var t;if(e)return t=(e=e.createElement("style")).ownerDocument.createTextNode("\n.______background-clip--text {\n  background-clip: text;\n  -webkit-background-clip: text;\n}\n"),e.appendChild(t),e}let g=["width","height","-webkit-text-fill-color"],p=["stroke","fill"];function ce(t,e,r){var{defaultComputedStyles:n,ownerDocument:o}=r,i=t.nodeName.toLowerCase(),l=C(t)&&"svg"!==i,a=l?p.map(e=>[e,t.getAttribute(e)]).filter(([,e])=>null!==e):[],u=[l&&"svg",i,a.map((e,t)=>e+"="+t).join(","),e].filter(Boolean).join(":");if(n.has(u))return n.get(u);let c=r.sandbox;if(!c)try{o&&((c=o.createElement("iframe")).id="__SANDBOX__-"+F(),c.width="0",c.height="0",c.style.visibility="hidden",c.style.position="fixed",o.body.appendChild(c),null!=(s=c.contentWindow)&&s.document.write('<!DOCTYPE html><meta charset="UTF-8"><title></title><body>'),r.sandbox=c)}catch(t){L("Failed to create iframe sandbox",t)}if(!c)return new Map;o=c.contentWindow;if(!o)return new Map;var s=o.document;let d,f;l?(d=s.createElementNS(_,"svg"),f=d.ownerDocument.createElementNS(d.namespaceURI,i),a.forEach(([e,t])=>{f.setAttributeNS(null,e,t)}),d.appendChild(f)):d=f=s.createElement(i),f.textContent=" ",s.body.appendChild(d);var h=o.getComputedStyle(f,e),m=new Map;for(let e=h.length,t=0;t<e;t++){let e=h.item(t);g.includes(e)||m.set(e,h.getPropertyValue(e))}return s.body.removeChild(d),n.set(u,m),m}function se(i,e,t){let r,l=new Map,a=[],u=new Map;if(t)for(let e of t)n(e);else for(let e=i.length,t=0;t<e;t++)n(i.item(t));for(let e=a.length,t=0;t<e;t++)null!=(r=u.get(a[t]))&&r.forEach((e,t)=>l.set(t,e));function n(t){var r=i.getPropertyValue(t),n=i.getPropertyPriority(t),o=t.lastIndexOf("-"),o=-1<o?t.substring(0,o):void 0;if(o){let e=u.get(o);e||(e=new Map,u.set(o,e)),e.set(t,[r,n])}e.get(t)===r&&!n||(o?a.push(o):l.set(t,[r,n]))}return l}let j=[":before",":after"],I=[":-webkit-scrollbar",":-webkit-scrollbar-button",":-webkit-scrollbar-thumb",":-webkit-scrollbar-track",":-webkit-scrollbar-track-piece",":-webkit-scrollbar-corner",":-webkit-resizer"];function de(t){if(t.ownerDocument)try{let e=t.toDataURL();if("data:,"!==e)return re(e,t.ownerDocument)}catch(t){}let e=t.cloneNode(!1),r=t.getContext("2d"),n=e.getContext("2d");try{r&&n&&n.putImageData(r.getImageData(0,0,t.width,t.height),0,0)}catch(t){L("Failed to clone canvas",t)}return e}let m=new Set(["symbol"]);function fe(c,s,d,f){return X(this,null,function*(){var e,t,r,n,o,i,l,a,u;A(d)&&("STYLE"===d.tagName||"SCRIPT"===d.tagName)||f.filter&&!f.filter(d)||(m.has(s.nodeName)||m.has(d.nodeName)?f.currentParentNodeStyle=void 0:f.currentParentNodeStyle=f.currentNodeStyle,e=yield me(d,f),f.isEnable("restoreScrollPosition")&&(t=c,r=e,T(t))&&T(r)&&({scrollTop:t,scrollLeft:n}=t,t||n)&&(o=r.style["transform"],{a:i,b:l,c:a,d:u}=o=new DOMMatrix(o),o.a=1,o.b=0,o.c=0,o.d=1,o.translateSelf(-n,-t),o.a=i,o.b=l,o.c=a,o.d=u,r.style.transform=o.toString()),s.appendChild(e))})}function he(r,n,o){return X(this,null,function*(){var t;for(let e=null!=(t=!A(r)||null==(t=r.shadowRoot)?void 0:t.firstChild)?t:r.firstChild;e;e=e.nextSibling)if(!s(e))if(A(e)&&d(e)&&"function"==typeof e.assignedNodes){let t=e.assignedNodes();for(let e=0;e<t.length;e++)yield fe(r,n,t[e],o)}else yield fe(r,n,e,o)})}let R=/^[\w-:]+$/;function me(w,v,b=!1){return X(this,null,function*(){let o,i,e,l,{ownerDocument:t,ownerWindow:r,fontFamilies:a}=v;if(t&&3===w.nodeType)return t.createTextNode(w.data);if(t&&r&&A(w)&&(T(w)||C(w))){let n=yield function(e,t){if("CANVAS"===e.tagName)return de(e);if("IFRAME"!==e.tagName)return k(e)?(t=(r=e).cloneNode(!1),r.currentSrc&&r.currentSrc!==r.src&&(t.src=r.currentSrc,t.srcset=""),"lazy"===t.loading&&(t.loading="eager"),t):D(e)?function(o){return X(this,null,function*(){if(o.ownerDocument&&!o.currentSrc&&o.poster)return re(o.poster,o.ownerDocument);let t=o.cloneNode(!1);t.crossOrigin="anonymous",o.currentSrc&&o.currentSrc!==o.src&&(t.src=o.currentSrc);var r=t.ownerDocument;if(r){let e=!0;if(yield ne(t,{onError:()=>e=!1}),!e)return o.poster?re(o.poster,o.ownerDocument):t;t.currentTime=o.currentTime,yield new Promise(e=>{t.addEventListener("seeked",e,{once:!0})});var n=r.createElement("canvas");n.width=o.offsetWidth,n.height=o.offsetHeight;try{let e=n.getContext("2d");e&&e.drawImage(t,0,0,n.width,n.height)}catch(r){return L("Failed to clone video",r),o.poster?re(o.poster,o.ownerDocument):t}return de(n)}return t})}(e):e.cloneNode(!1);var r,n=e;try{if(null!=(r=null==n?void 0:n.contentDocument)&&r.body)return me(n.contentDocument.body,t)}catch(n){L("Failed to clone iframe",n)}return n.cloneNode(!1)}(w,v);if(v.isEnable("removeAbnormalAttributes")){let r=n.getAttributeNames();for(let e=r.length,t=0;t<e;t++){let e=r[t];R.test(e)||n.removeAttribute(e)}}let t=v.currentNodeStyle=function(e,t,r,n){let o,i,l,a,{ownerWindow:u,includeStyleProperties:c,currentParentNodeStyle:s}=n,d=t.style,f=u.getComputedStyle(e),h=ce(e,null,n);null!=s&&s.forEach((e,t)=>{h.delete(t)});n=se(f,h,c);return n.delete("transition-property"),n.delete("all"),n.delete("d"),n.delete("content"),r&&(n.delete("margin-top"),n.delete("margin-right"),n.delete("margin-bottom"),n.delete("margin-left"),n.delete("margin-block-start"),n.delete("margin-block-end"),n.delete("margin-inline-start"),n.delete("margin-inline-end"),n.set("box-sizing",["border-box",""])),"text"===(null==(o=n.get("background-clip"))?void 0:o[0])&&t.classList.add("______background-clip--text"),E&&(n.has("font-kerning")||n.set("font-kerning",["normal",""]),"hidden"===(null==(i=n.get("overflow-x"))?void 0:i[0])||"hidden"===(null==(l=n.get("overflow-y"))?void 0:l[0]))&&"ellipsis"===(null==(a=n.get("text-overflow"))?void 0:a[0])&&e.scrollWidth===e.clientWidth&&n.set("text-overflow",["clip",""]),n.forEach(([e,t],r)=>{d.setProperty(r,e,t)}),n}(w,n,b,v);if(b){var c=n;var{backgroundColor:u,width:s,height:d,style:f}=v,h=c.style;if(u&&h.setProperty("background-color",u,"important"),s&&h.setProperty("width",s+"px","important"),d&&h.setProperty("height",d+"px","important"),f)for(let e in f)h[e]=f[e]}let r=!1;if(v.isEnable("copyScrollbar")){let e=[null==(o=t.get("overflow-x"))?void 0:o[0],null==(i=t.get("overflow-y"))?void 0:i[1]];r=e.includes("scroll")||(e.includes("auto")||e.includes("overlay"))&&(w.scrollHeight>w.clientHeight||w.scrollWidth>w.clientWidth)}{var m=w;var g=n;c=r;var p=v;let{ownerWindow:t,svgStyleElement:e,svgStyles:a,currentNodeStyle:u}=p;function y(o){var e=t.getComputedStyle(m,o);let i=e.getPropertyValue("content");if(i&&"none"!==i){i=i.replace(/(')|(")|(counter\(.+\))/g,"");let t=[F()],r=ce(m,o,p);null!=u&&u.forEach((e,t)=>{r.delete(t)});e=se(e,r,p.includeStyleProperties);e.delete("content"),e.delete("-webkit-locale"),"text"===(null==(l=e.get("background-clip"))?void 0:l[0])&&g.classList.add("______background-clip--text");let n=[`content: '${i}';`];if(e.forEach(([e,t],r)=>{n.push(r+`: ${e}${t?" !important":""};`)}),1!==n.length){try{g.className=[g.className,...t].join(" ")}catch(e){return}var l=n.join("\n  ");let e=a.get(l);e||(e=[],a.set(l,e)),e.push(`.${t[0]}:`+o)}}}e&&t&&(j.forEach(y),c)&&I.forEach(y)}return u=w,s=n,P(u)&&(s.innerHTML=u.value),!P(u)&&"INPUT"!==u.tagName&&"SELECT"!==u.tagName||s.setAttribute("value",u.value),null!=(l=ie(null==(e=t.get("font-family"))?void 0:e[0]))&&l.forEach(e=>a.add(e)),D(w)||(yield he(w,n,v)),n}d=w.cloneNode(!1);return yield he(w,d,v),d})}function ge(e){if(e.ownerDocument=void 0,e.ownerWindow=void 0,e.svgStyleElement=void 0,e.svgDefsElement=void 0,e.svgStyles.clear(),e.defaultComputedStyles.clear(),e.sandbox){try{e.sandbox.remove()}catch(e){}e.sandbox=void 0}e.workers=[],e.fontFamilies.clear(),e.fontCssTexts.clear(),e.requests.clear(),e.tasks=[]}function pe(e,t){let{url:r,requestType:n="text",responseType:o="text",imageDom:i}=t,l=r,{timeout:u,acceptOfImage:c,requests:s,fetchFn:d,fetch:{requestInit:f,bypassingCache:h,placeholderImage:m},workers:g}=e,p=("image"===n&&(w||x)&&e.drawImageCount++,s.get(r));if(!p){h&&h instanceof RegExp&&h.test(l)&&(l+=(/\?/.test(l)?"&":"?")+(new Date).getTime());let a=G({url:l,timeout:u,responseType:o,headers:"image"===n?{accept:c}:void 0},f);(p={type:n,resolve:void 0,reject:void 0,response:null}).response=X(this,null,function*(){if(d&&"image"===n){let e=yield d(r);if(e)return e}if(!w&&r.startsWith("http")&&g.length)return new Promise((e,t)=>{g[s.size&g.length-1].postMessage(G({rawUrl:r},a)),p.resolve=e,p.reject=t});{let e=a,{url:t,timeout:r,responseType:n}=e,o=((e,t)=>{var r={};for(n in e)V.call(e,n)&&t.indexOf(n)<0&&(r[n]=e[n]);if(null!=e&&$)for(var n of $(e))t.indexOf(n)<0&&z.call(e,n)&&(r[n]=e[n]);return r})(e,["url","timeout","responseType"]),i=new AbortController,l=r?setTimeout(()=>i.abort(),r):void 0;return fetch(t,G({signal:i.signal},o)).then(e=>{if(e.ok)return"dataUrl"!==n?e.text():e.blob().then(y);throw new Error("Failed fetch, not 2xx response",{cause:e})}).finally(()=>clearTimeout(l))}}).catch(e=>{if(s.delete(r),"image"===n&&m)return L("Failed to fetch image base64, trying to use placeholder image",l),"string"==typeof m?m:m(i);throw e}),s.set(r,p)}return p.response}function ye(i,e,n,o){return X(this,null,function*(){if(we(i))for(var[t,r]of function(n){let o=[];return i.replace(U,(e,t,r)=>(o.push([r,K(r,n)]),e)),o.filter(([e])=>!O(e))}(e))try{let e=yield pe(n,{url:r,requestType:o?"image":"text",responseType:"dataUrl"});i=i.replace(function(e){e=e.replace(/([.*+?^${}()|\[\]\/\\])/g,"\\$1");return new RegExp(`(url\\(['"]?)(${e})(['"]?\\))`,"g")}(t),`$1${e}$3`)}catch(e){L("Failed to fetch css data url",t,e)}return i})}function we(e){return/url\((['"]?)([^'"]+?)\1\)/.test(e)}let U=/url\((['"]?)([^'"]+?)\1\)/g,B=/(\/\*[\s\S]*?\*\/)/gi,M=/((@.*?keyframes [\s\S]*?){([\s\S]*?}\s*?)})/gi,o=/url\([^)]+\)\s*format\((["']?)([^"']+)\1\)/g,W=/src:\s*(?:url\([^)]+\)\s*format\([^)]+\)[,;]\s*)+/g;function ve(e,t){let r=t["font"],n=!r||null==r?void 0:r.preferredFormat;return n?e.replace(W,e=>{for(;;){var[t,,r]=o.exec(e)||[];if(!r)return"";if(r===n)return`src: ${t};`}}):e}let q=["background-image","border-image-source","-webkit-border-image","-webkit-mask-image","list-style-image"];function Te(p,y){return X(this,null,function*(){var n=yield le(p,y);if(A(n.node)&&C(n.node))return n.node;let{ownerDocument:e,log:t,tasks:r,svgStyleElement:o,svgDefsElement:i,svgStyles:l,font:a,progress:u,autoDestruct:c,onCloneNode:s,onEmbedNode:d,onCreateForeignObjectSvg:f}=n;t.time("clone node");var h=yield me(n.node,n,!0);if(o&&e){let r="";l.forEach((e,t)=>{r+=e.join(",\n")+` {
  ${t}
}
`}),o.appendChild(e.createTextNode(r))}t.timeEnd("clone node"),null!=s&&s(h),!1!==a&&A(h)&&(t.time("embed web font"),yield function(a){return X(this,null,function*(){let{ownerDocument:n,svgStyleElement:o,fontFamilies:t,fontCssTexts:i,tasks:l,font:r}=a;if(n&&o&&t.size)if(r&&r.cssText){let e=ve(r.cssText,a);o.appendChild(n.createTextNode(e+"\n"))}else{let e=Array.from(n.styleSheets).filter(t=>{try{return"cssRules"in t&&Boolean(t.cssRules.length)}catch(e){return L("Error while reading CSS rules from "+t.href,e),!1}});yield Promise.all(e.flatMap(i=>Array.from(i.cssRules).map((t,o)=>X(this,null,function*(){if("CSSImportRule"===t.constructor.name){let e=o+1,n=t.href,r="";try{r=yield pe(a,{url:n,requestType:"text",responseType:"text"})}catch(e){L("Error fetch remote css import from "+n,e)}for(let t of function(e){if(null==e)return[];var t=[];let r=e.replace(B,"");for(;;){let e=M.exec(r);if(!e)break;t.push(e[0])}r=r.replace(M,"");for(var n=/@import[\s\S]*?url\([^)]*\)[\s\S]*?;/gi,o=new RegExp("((\\s*?(?:\\/\\*[\\s\\S]*?\\*\\/)?\\s*?@media[\\s\\S]*?){([\\s\\S]*?)}\\s*?})|(([\\s\\S]*?){([\\s\\S]*?)})","gi");;){let e=n.exec(r);if(e)o.lastIndex=n.lastIndex;else{if(!(e=o.exec(r)))break;n.lastIndex=o.lastIndex}t.push(e[0])}return t}(r.replace(U,(e,t,r)=>e.replace(r,K(r,n)))))try{i.insertRule(t,t.startsWith("@import")?e+=1:i.cssRules.length)}catch(e){L("Error inserting rule from remote css import",{rule:t,error:e})}}})))),e.flatMap(e=>Array.from(e.cssRules)).filter(e=>{return"CSSFontFaceRule"===e.constructor.name&&we(e.style.getPropertyValue("src"))&&(null==(e=ie(e.style.getPropertyValue("font-family")))?void 0:e.some(e=>t.has(e)))}).forEach(e=>{let t=e,r=i.get(t.cssText);r?o.appendChild(n.createTextNode(r+"\n")):l.push(ye(t.cssText,t.parentStyleSheet?t.parentStyleSheet.href:null,a).then(e=>{e=ve(e,a),i.set(t.cssText,e),o.appendChild(n.createTextNode(e+"\n"))}))})}})}(n),t.timeEnd("embed web font")),t.time("embed node"),function t(e,r){var n,o,i=r.tasks;A(e)&&((k(e)||N(e))&&i.push(...function(r,e){if(k(r)){let t=r.currentSrc||r.src;if(!O(t))return[pe(e,{url:t,imageDom:r,requestType:"image",responseType:"dataUrl"}).then(e=>{e&&(r.srcset="",r.dataset.originalSrc=t,r.src=e||"")})];(w||x)&&e.drawImageCount++}else if(C(r)&&!O(r.href.baseVal)){let t=r.href.baseVal;return[pe(e,{url:t,imageDom:r,requestType:"image",responseType:"dataUrl"}).then(e=>{e&&(r.dataset.originalSrc=t,r.href.baseVal=e||"")})]}return[]}(e,r)),"use"===e.tagName)&&i.push(...function(r,n){var e;let{ownerDocument:o,svgDefsElement:i}=n,t=null!=(e=r.getAttribute("href"))?e:r.getAttribute("xlink:href");if(t){var[l,a]=t.split("#");if(a){let e="#"+a,t=null==o?void 0:o.querySelector("svg "+e);if(l&&r.setAttribute("href",e),null!=i&&i.querySelector(e))return[];if(t)return null!=i&&i.appendChild(t.cloneNode(!0)),[];if(l)return[pe(n,{url:l,responseType:"text"}).then(e=>{null!=i&&i.insertAdjacentHTML("beforeend",e)})]}}return[]}(e,r)),T(e)&&i.push(...(n=e.style,o=r,q.map(t=>{let r=n.getPropertyValue(t);return r&&"none"!==r?((w||x)&&o.drawImageCount++,ye(r,null,o,!0).then(e=>{e&&r!==e&&n.setProperty(t,e,n.getPropertyPriority(t))})):null}).filter(Boolean))),e.childNodes.forEach(e=>{t(e,r)})}(h,n);let m=r.length,g=0;null!=u&&u(g,m),yield Promise.all([...Array(4)].map(()=>X(this,null,function*(){for(;;){var e=r.pop();if(!e)break;try{yield e}catch(e){L("Failed to run task",e)}null!=u&&u(++g,m)}}))),t.timeEnd("embed node"),null!=d&&d(h);h=function(e){var{width:t,height:r}=n,t=Z(t,r,e.ownerDocument),r=t.ownerDocument.createElementNS(t.namespaceURI,"foreignObject");return r.setAttributeNS(null,"x","0%"),r.setAttributeNS(null,"y","0%"),r.setAttributeNS(null,"width","100%"),r.setAttributeNS(null,"height","100%"),r.append(e),t.appendChild(r),t}(h);return i&&h.insertBefore(i,h.children[0]),o&&h.insertBefore(o,h.children[0]),c&&ge(n),null!=f&&f(h),h})}function be(o,i){return X(this,null,function*(){var e=yield le(o,i),t=yield Te(e),r=ee(t,e.isEnable("removeControlCharacter")),n=(e.autoDestruct||(e.svgStyleElement=ue(e.ownerDocument),e.svgDefsElement=null==(n=e.ownerDocument)?void 0:n.createElementNS(_,"defs"),e.svgStyles.clear()),re(r,t.ownerDocument));return yield function(u,c){return X(this,null,function*(){let{log:e,timeout:t,drawImageCount:r,drawImageInterval:n}=c,o=(e.time("image to canvas"),yield ne(u,{timeout:t})),{canvas:i,context2d:l}=function(e){var{width:t,height:r,scale:n,backgroundColor:o,maximumCanvasSize:i}=c,e=e.createElement("canvas"),n=(e.width=Math.floor(t*n),e.height=Math.floor(r*n),e.style.width=t+"px",e.style.height=r+"px",i&&(e.width>i||e.height>i)&&(e.width>i&&e.height>i?e.width>e.height?(e.height*=i/e.width,e.width=i):(e.width*=i/e.height,e.height=i):e.width>i?(e.height*=i/e.width,e.width=i):(e.width*=i/e.height,e.height=i)),e.getContext("2d"));return n&&o&&(n.fillStyle=o,n.fillRect(0,0,e.width,e.height)),{canvas:e,context2d:n}}(u.ownerDocument),a=()=>{try{null!=l&&l.drawImage(o,0,0,i.width,i.height)}catch(e){L("Failed to drawImage",e)}};if(a(),c.isEnable("fixSvgXmlDecode"))for(let t=0;t<r;t++)yield new Promise(e=>{setTimeout(()=>{a(),e()},t+n)});return c.drawImageCount=0,e.timeEnd("image to canvas"),i})}(n,e)})}function Se(o,i){return X(this,null,function*(){let e=yield le(o,i),{log:t,quality:r,type:u,dpi:c}=e,n=yield be(e),s=(t.time("canvas to data url"),n.toDataURL(u,r));if(["image/png","image/jpeg"].includes(u)&&c&&f&&h){let[e,t]=s.split(","),r=0,n=!1;if("image/png"===u){let e=function(e){let t=e.indexOf("AAlwSFlz");return t=-1===(t=-1===t?e.indexOf("AAAJcEhZ"):t)?e.indexOf("AAAACXBI"):t}(t);0<=e?(r=4*Math.ceil((e+28)/3),n=!0):r=44}else"image/jpeg"===u&&(r=24);let o=t.substring(0,r),i=t.substring(r),l=window.atob(o),a=new Uint8Array(l.length);for(let e=0;e<a.length;e++)a[e]=l.charCodeAt(e);var d="image/png"===u?J(a,c,n):Y(a,c);s=[e,",",window.btoa(String.fromCharCode(...d)),i].join("")}return t.timeEnd("canvas to data url"),s})}function ke(i,l){return X(this,null,function*(){var e=yield le(i,l),{width:t,height:r,ownerDocument:n}=e,o=yield Se(e),t=Z(t,r,n),r=t.ownerDocument.createElementNS(t.namespaceURI,"image");return r.setAttributeNS(null,"href",o),r.setAttributeNS(null,"height","100%"),r.setAttributeNS(null,"width","100%"),t.appendChild(r),ee(t,e.isEnable("removeControlCharacter"))})}t.createContext=ae,t.destroyContext=ge,t.domToBlob=function(t,l){return X(this,null,function*(){var r=yield le(t,l),{log:n,type:o,quality:e,dpi:i}=r,r=yield be(r),r=(n.time("canvas to blob"),yield Ne(r,o,e));if(["image/png","image/jpeg"].includes(o)&&i){let e=yield te(r.slice(0,33),"arrayBuffer"),t=new Uint8Array(e);return"image/png"===o?t=J(t,i):"image/jpeg"===o&&(t=Y(t,i)),n.timeEnd("canvas to blob"),new Blob([t,r.slice(33)],{type:o})}return n.timeEnd("canvas to blob"),r})},t.domToCanvas=be,t.domToDataUrl=Se,t.domToForeignObjectSvg=Te,t.domToImage=function(l,a){return X(this,null,function*(){var e=yield le(l,a),{ownerDocument:t,width:r,height:n,scale:o,type:i}=e,i=re("image/svg+xml"===i?yield ke(e):yield Se(e),t);return i.width=Math.floor(r*o),i.height=Math.floor(n*o),i.style.width=r+"px",i.style.height=n+"px",i})},t.domToJpeg=function(e,t){return X(this,null,function*(){return Se(yield le(e,H(G({},t),{type:"image/jpeg"})))})},t.domToPixel=function(t,r){return X(this,null,function*(){var e=yield be(yield le(t,r));return e.getContext("2d").getImageData(0,0,e.width,e.height).data})},t.domToPng=function(e,t){return X(this,null,function*(){return Se(yield le(e,H(G({},t),{type:"image/png"})))})},t.domToSvg=ke,t.domToWebp=function(e,t){return X(this,null,function*(){return Se(yield le(e,H(G({},t),{type:"image/webp"})))})},t.loadMedia=ne,t.waitUntilLoad=oe,Object.defineProperty(t,Symbol.toStringTag,{value:"Module"})}}}]);