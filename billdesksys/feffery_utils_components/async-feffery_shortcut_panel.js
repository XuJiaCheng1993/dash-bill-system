(window.webpackJsonpfeffery_utils_components=window.webpackJsonpfeffery_utils_components||[]).push([[29],{498:function(module,__webpack_exports__,__webpack_require__){__webpack_require__.r(__webpack_exports__);var react__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(1),react__WEBPACK_IMPORTED_MODULE_0___default=__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__),_components_FefferyShortcutPanel_react__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(181),lodash__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(25),lodash__WEBPACK_IMPORTED_MODULE_2___default=__webpack_require__.n(lodash__WEBPACK_IMPORTED_MODULE_2__),ninja_keys__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(913),_components_FefferyStyle_react__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(92);function _typeof(e){return(_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function ownKeys(t,e){var i,n=Object.keys(t);return Object.getOwnPropertySymbols&&(i=Object.getOwnPropertySymbols(t),e&&(i=i.filter(function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable})),n.push.apply(n,i)),n}function _objectSpread(t){for(var e=1;e<arguments.length;e++){var i=null!=arguments[e]?arguments[e]:{};e%2?ownKeys(Object(i),!0).forEach(function(e){_defineProperty(t,e,i[e])}):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(i)):ownKeys(Object(i)).forEach(function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(i,e))})}return t}function _defineProperty(e,t,i){(t=_toPropertyKey(t))in e?Object.defineProperty(e,t,{value:i,enumerable:!0,configurable:!0,writable:!0}):e[t]=i}function _toPropertyKey(e){e=_toPrimitive(e,"string");return"symbol"==_typeof(e)?e:e+""}function _toPrimitive(e,t){if("object"!=_typeof(e)||!e)return e;var i=e[Symbol.toPrimitive];if(void 0===i)return("string"===t?String:Number)(e);i=i.call(e,t||"default");if("object"!=_typeof(i))return i;throw new TypeError("@@toPrimitive must return a primitive value.")}var footerHtmlEn=react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div",{class:"modal-footer",slot:"footer"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{class:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"enter"),"to select"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",className:"ninja-examplekey",viewBox:"0 0 24 24"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M0 0h24v24H0V0z",fill:"none"}),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"})),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",className:"ninja-examplekey",viewBox:"0 0 24 24"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M0 0h24v24H0V0z",fill:"none"}),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z"})),"to navigate"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"esc"),"to close"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"backspace"),"move to parent")),footerHtmlZh=react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div",{className:"modal-footer",slot:"footer"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"enter"),"选择"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",className:"ninja-examplekey",viewBox:"0 0 24 24"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M0 0h24v24H0V0z",fill:"none"}),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"})),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",className:"ninja-examplekey",viewBox:"0 0 24 24"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M0 0h24v24H0V0z",fill:"none"}),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("path",{d:"M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z"})),"上下切换"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"esc"),"关闭面板"),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"help"},react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span",{className:"ninja-examplekey esc"},"backspace"),"回到上一级")),locale2footer=new Map([["en",footerHtmlEn],["zh",footerHtmlZh]]),locale2placeholder=new Map([["en","Type a command or search..."],["zh","输入指令或进行搜索..."]]),FefferyShortcutPanel=function FefferyShortcutPanel(props){var id=props.id,data=props.data,placeholder=props.placeholder,openHotkey=props.openHotkey,theme=props.theme,locale=props.locale,open=props.open,close=props.close,panelStyles=props.panelStyles,setProps=props.setProps,loading_state=props.loading_state,data=data.map(function(e){return Object(lodash__WEBPACK_IMPORTED_MODULE_2__.isString)(e.handler)||e.hasOwnProperty("children")?e:_objectSpread(_objectSpread({},e),{handler:function(){setProps({triggeredHotkey:{id:e.id,timestamp:Date.parse(new Date)}})}})}),ninjaKeys=Object(react__WEBPACK_IMPORTED_MODULE_0__.useRef)(null);return Object(react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){ninjaKeys.current&&ninjaKeys.current.addEventListener("change",function(e){setProps({searchValue:e.detail.search})})},[]),Object(react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){ninjaKeys.current&&(ninjaKeys.current.data=data.map(function(item){return Object(lodash__WEBPACK_IMPORTED_MODULE_2__.isString)(item.handler)?_objectSpread(_objectSpread({},item),{handler:eval(item.handler)}):item}))},[data]),Object(react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){ninjaKeys.current&&open&&(ninjaKeys.current.open(),setProps({open:!1}))},[open]),Object(react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(function(){ninjaKeys.current&&close&&(ninjaKeys.current.close(),setProps({close:!1}))},[close]),panelStyles=_objectSpread(_objectSpread({},{width:"640px",overflowBackground:"rgba(255, 255, 255, 0.5)",textColor:"rgb(60, 65, 73)",fontSize:"16px",top:"20%",accentColor:"rgb(110, 94, 210)",secondaryBackgroundColor:"rgb(239, 241, 244)",secondaryTextColor:"rgb(107, 111, 118)",selectedBackground:"rgb(248, 249, 251)",actionsHeight:"300px",groupTextColor:"rgb(144, 149, 157)",zIndex:1}),panelStyles),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react__WEBPACK_IMPORTED_MODULE_0___default.a.Fragment,null,react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_components_FefferyStyle_react__WEBPACK_IMPORTED_MODULE_4__.a,{rawStyle:"\nninja-keys {\n    --ninja-width: ".concat(panelStyles.width,";\n    --ninja-overflow-background: ").concat(panelStyles.overflowBackground,";\n    --ninja-text-color: ").concat(panelStyles.textColor,";\n    --ninja-font-size: ").concat(panelStyles.fontSize,";\n    --ninja-top: ").concat(panelStyles.top,";\n    --ninja-accent-color: ").concat(panelStyles.accentColor,";\n    --ninja-secondary-background-color: ").concat(panelStyles.secondaryBackgroundColor,";\n    --ninja-secondary-text-color: ").concat(panelStyles.secondaryTextColor,";\n    --ninja-selected-background: ").concat(panelStyles.selectedBackground,";\n    --ninja-actions-height: ").concat(panelStyles.actionsHeight,";\n    --ninja-group-text-color: ").concat(panelStyles.groupTextColor,";\n    --ninja-z-index: ").concat(panelStyles.zIndex,";\n}\n")}),react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("ninja-keys",{id:id,class:theme,ref:ninjaKeys,placeholder:placeholder||locale2placeholder.get(locale),openHotkey:openHotkey,hotKeysJoinedView:!0,hideBreadcrumbs:!0,"data-dash-is-loading":loading_state&&loading_state.is_loading||void 0},locale2footer.get(locale)))};__webpack_exports__.default=FefferyShortcutPanel,FefferyShortcutPanel.defaultProps=_components_FefferyShortcutPanel_react__WEBPACK_IMPORTED_MODULE_1__.b,FefferyShortcutPanel.propTypes=_components_FefferyShortcutPanel_react__WEBPACK_IMPORTED_MODULE_1__.c},913:function(T,R,e){let B=window,L=B.ShadowRoot&&(void 0===B.ShadyCSS||B.ShadyCSS.nativeShadow)&&"adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,I=Symbol(),K=new WeakMap;class N{constructor(e,t,i){if(this._$cssResult$=!0,i!==I)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=e,this.t=t}get styleSheet(){let e=this.o;var t,i=this.t;return L&&void 0===e&&(t=void 0!==i&&1===i.length,void 0===(e=t?K.get(i):e))&&((this.o=e=new CSSStyleSheet).replaceSync(this.cssText),t)&&K.set(i,e),e}toString(){return this.cssText}}let z=(n,...e)=>{e=1===n.length?n[0]:e.reduce((e,t,i)=>e+(()=>{if(!0===t._$cssResult$)return t.cssText;if("number"==typeof t)return t;throw Error("Value passed to 'css' function must be a 'css' function result: "+t+". Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.")})()+n[i+1],n[0]);return new N(e,n,I)},W=L?e=>e:t=>{if(!(t instanceof CSSStyleSheet))return t;{let e="";for(var i of t.cssRules)e+=i.cssText;return t=e,new N("string"==typeof t?t:t+"",void 0,I)}},V,q=window,F=q.trustedTypes,J=F?F.emptyScript:"",G=q.reactiveElementPolyfillSupport,Z={toAttribute(e,t){switch(t){case Boolean:e=e?J:null;break;case Object:case Array:e=null==e?e:JSON.stringify(e)}return e},fromAttribute(e,t){let i=e;switch(t){case Boolean:i=null!==e;break;case Number:i=null===e?null:Number(e);break;case Object:case Array:try{i=JSON.parse(e)}catch(e){i=null}}return i}},Q=(e,t)=>t!==e&&(t==t||e==e),X={attribute:!0,type:String,converter:Z,reflect:!1,hasChanged:Q};class t extends HTMLElement{constructor(){super(),this._$Ei=new Map,this.isUpdatePending=!1,this.hasUpdated=!1,this._$El=null,this._$Eu()}static addInitializer(e){var t;this.finalize(),(null!=(t=this.h)?t:this.h=[]).push(e)}static get observedAttributes(){this.finalize();let i=[];return this.elementProperties.forEach((e,t)=>{e=this._$Ep(t,e);void 0!==e&&(this._$Ev.set(e,t),i.push(e))}),i}static createProperty(e,t=X){var i;t.state&&(t.attribute=!1),this.finalize(),this.elementProperties.set(e,t),t.noAccessor||this.prototype.hasOwnProperty(e)||(i="symbol"==typeof e?Symbol():"__"+e,void 0!==(i=this.getPropertyDescriptor(e,i,t))&&Object.defineProperty(this.prototype,e,i))}static getPropertyDescriptor(i,n,s){return{get(){return this[n]},set(e){var t=this[i];this[n]=e,this.requestUpdate(i,t,s)},configurable:!0,enumerable:!0}}static getPropertyOptions(e){return this.elementProperties.get(e)||X}static finalize(){if(this.hasOwnProperty("finalized"))return!1;this.finalized=!0;let e=Object.getPrototypeOf(this);if(e.finalize(),void 0!==e.h&&(this.h=[...e.h]),this.elementProperties=new Map(e.elementProperties),this._$Ev=new Map,this.hasOwnProperty("properties")){let e=this.properties,t=[...Object.getOwnPropertyNames(e),...Object.getOwnPropertySymbols(e)];for(var i of t)this.createProperty(i,e[i])}return this.elementStyles=this.finalizeStyles(this.styles),!0}static finalizeStyles(e){var t=[];if(Array.isArray(e)){var i=new Set(e.flat(1/0).reverse());for(let e of i)t.unshift(W(e))}else void 0!==e&&t.push(W(e));return t}static _$Ep(e,t){t=t.attribute;return!1===t?void 0:"string"==typeof t?t:"string"==typeof e?e.toLowerCase():void 0}_$Eu(){var e;this._$E_=new Promise(e=>this.enableUpdating=e),this._$AL=new Map,this._$Eg(),this.requestUpdate(),null!=(e=this.constructor.h)&&e.forEach(e=>e(this))}addController(e){var t;(null!=(t=this._$ES)?t:this._$ES=[]).push(e),void 0!==this.renderRoot&&this.isConnected&&null!=(t=e.hostConnected)&&t.call(e)}removeController(e){var t;null!=(t=this._$ES)&&t.splice(this._$ES.indexOf(e)>>>0,1)}_$Eg(){this.constructor.elementProperties.forEach((e,t)=>{this.hasOwnProperty(t)&&(this._$Ei.set(t,this[t]),delete this[t])})}createRenderRoot(){var n,e,t=null!=(t=this.shadowRoot)?t:this.attachShadow(this.constructor.shadowRootOptions);return n=t,e=this.constructor.elementStyles,L?n.adoptedStyleSheets=e.map(e=>e instanceof CSSStyleSheet?e:e.styleSheet):e.forEach(e=>{var t=document.createElement("style"),i=B.litNonce;void 0!==i&&t.setAttribute("nonce",i),t.textContent=e.cssText,n.appendChild(t)}),t}connectedCallback(){var e;void 0===this.renderRoot&&(this.renderRoot=this.createRenderRoot()),this.enableUpdating(!0),null!=(e=this._$ES)&&e.forEach(e=>{var t;return null==(t=e.hostConnected)?void 0:t.call(e)})}enableUpdating(e){}disconnectedCallback(){var e;null!=(e=this._$ES)&&e.forEach(e=>{var t;return null==(t=e.hostDisconnected)?void 0:t.call(e)})}attributeChangedCallback(e,t,i){this._$AK(e,i)}_$EO(e,t,i=X){var n,s=this.constructor._$Ep(e,i);void 0!==s&&!0===i.reflect&&(n=(void 0!==(null==(n=i.converter)?void 0:n.toAttribute)?i.converter:Z).toAttribute(t,i.type),this._$El=e,null==n?this.removeAttribute(s):this.setAttribute(s,n),this._$El=null)}_$AK(e,i){var n=this.constructor,s=n._$Ev.get(e);if(void 0!==s&&this._$El!==s){let e=n.getPropertyOptions(s),t="function"==typeof e.converter?{fromAttribute:e.converter}:void 0!==(null==(n=e.converter)?void 0:n.fromAttribute)?e.converter:Z;this._$El=s,this[s]=t.fromAttribute(i,e.type),this._$El=null}}requestUpdate(e,t,i){let n=!0;void 0!==e&&(((i=i||this.constructor.getPropertyOptions(e)).hasChanged||Q)(this[e],t)?(this._$AL.has(e)||this._$AL.set(e,t),!0===i.reflect&&this._$El!==e&&(void 0===this._$EC&&(this._$EC=new Map),this._$EC.set(e,i))):n=!1),!this.isUpdatePending&&n&&(this._$E_=this._$Ej())}async _$Ej(){this.isUpdatePending=!0;try{await this._$E_}catch(e){Promise.reject(e)}var e=this.scheduleUpdate();return null!=e&&await e,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){var t;if(this.isUpdatePending){this.hasUpdated,this._$Ei&&(this._$Ei.forEach((e,t)=>this[t]=e),this._$Ei=void 0);let e=!1;var i=this._$AL;try{(e=this.shouldUpdate(i))?(this.willUpdate(i),null!=(t=this._$ES)&&t.forEach(e=>{var t;return null==(t=e.hostUpdate)?void 0:t.call(e)}),this.update(i)):this._$Ek()}catch(t){throw e=!1,this._$Ek(),t}e&&this._$AE(i)}}willUpdate(e){}_$AE(e){var t;null!=(t=this._$ES)&&t.forEach(e=>{var t;return null==(t=e.hostUpdated)?void 0:t.call(e)}),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(e)),this.updated(e)}_$Ek(){this._$AL=new Map,this.isUpdatePending=!1}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$E_}shouldUpdate(e){return!0}update(e){void 0!==this._$EC&&(this._$EC.forEach((e,t)=>this._$EO(t,this[t],e)),this._$EC=void 0),this._$Ek()}updated(e){}firstUpdated(e){}}t.finalized=!0,t.elementProperties=new Map,t.elementStyles=[],t.shadowRootOptions={mode:"open"},null!=G&&G({ReactiveElement:t}),(null!=(V=q.reactiveElementVersions)?V:q.reactiveElementVersions=[]).push("1.6.3");let Y=window,c=Y.trustedTypes,ee=c?c.createPolicy("lit-html",{createHTML:e=>e}):void 0,p=`lit$${(Math.random()+"").slice(9)}$`,te="?"+p,ie=`<${te}>`,l=document,h=()=>l.createComment(""),d=e=>null===e||"object"!=typeof e&&"function"!=typeof e,ne=Array.isArray,se=e=>ne(e)||"function"==typeof(null==e?void 0:e[Symbol.iterator]),u=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,re=/-->/g,oe=/>/g,_=RegExp(">|[ \t\n\f\r](?:([^\\s\"'>=/]+)([ \t\n\f\r]*=[ \t\n\f\r]*(?:[^ \t\n\f\r\"'`<>=]|(\"|')|))|$)","g"),ae=/'/g,le=/"/g,ce=/^(?:script|style|textarea|title)$/i,he=i=>(e,...t)=>({_$litType$:i,strings:e,values:t}),r=he(1),f=(he(2),Symbol.for("lit-noChange")),v=Symbol.for("lit-nothing"),de=new WeakMap,y=l.createTreeWalker(l,129,null,!1);function pe(e,t){if(Array.isArray(e)&&e.hasOwnProperty("raw"))return void 0!==ee?ee.createHTML(t):t;throw Error("invalid template strings array")}let ue=(o,e)=>{let t=o.length-1,a=[],l,c=2===e?"<svg>":"",h=u;for(let r=0;r<t;r++){let e=o[r],t,i,n=-1,s=0;for(;s<e.length&&(h.lastIndex=s,null!==(i=h.exec(e)));)s=h.lastIndex,h===u?"!--"===i[1]?h=re:void 0!==i[1]?h=oe:void 0!==i[2]?(ce.test(i[2])&&(l=RegExp("</"+i[2],"g")),h=_):void 0!==i[3]&&(h=_):h===_?">"===i[0]?(h=null!=l?l:u,n=-1):void 0===i[1]?n=-2:(n=h.lastIndex-i[2].length,t=i[1],h=void 0===i[3]?_:'"'===i[3]?le:ae):h===le||h===ae?h=_:h===re||h===oe?h=u:(h=_,l=void 0);var d=h===_&&o[r+1].startsWith("/>")?" ":"";c+=h===u?e+ie:0<=n?(a.push(t),e.slice(0,n)+"$lit$"+e.slice(n)+p+d):e+p+(-2===n?(a.push(void 0),r):d)}return[pe(o,c+(o[t]||"<?>")+(2===e?"</svg>":"")),a]};class _e{constructor({strings:e,_$litType$:t},i){var n;this.parts=[];let s=0,r=0;var o=e.length-1,a=this.parts,[e,l]=ue(e,t);if(this.el=_e.createElement(e,i),y.currentNode=this.el.content,2===t){let e=this.el.content,t=e.firstChild;t.remove(),e.append(...t.childNodes)}for(;null!==(n=y.nextNode())&&a.length<o;){if(1===n.nodeType){if(n.hasAttributes()){let t=[];for(let e of n.getAttributeNames())if(e.endsWith("$lit$")||e.startsWith(p)){let i=l[r++];if(t.push(e),void 0!==i){let e=n.getAttribute(i.toLowerCase()+"$lit$").split(p),t=/([.?@])?(.*)/.exec(i);a.push({type:1,index:s,name:t[2],strings:e,ctor:"."===t[1]?me:"?"===t[1]?$e:"@"===t[1]?be:ye})}else a.push({type:6,index:s})}for(let e of t)n.removeAttribute(e)}if(ce.test(n.tagName)){let t=n.textContent.split(p),i=t.length-1;if(0<i){n.textContent=c?c.emptyScript:"";for(let e=0;e<i;e++)n.append(t[e],h()),y.nextNode(),a.push({type:2,index:++s});n.append(t[i],h())}}}else if(8===n.nodeType)if(n.data===te)a.push({type:2,index:s});else{let e=-1;for(;-1!==(e=n.data.indexOf(p,e+1));)a.push({type:7,index:s}),e+=p.length-1}s++}}static createElement(e,t){var i=l.createElement("template");return i.innerHTML=e,i}}function m(t,i,n=t,s){var r;if(i!==f){let e=void 0!==s?null==(o=n._$Co)?void 0:o[s]:n._$Cl;var o=d(i)?void 0:i._$litDirective$;(null==e?void 0:e.constructor)!==o&&(null!=(r=null==e?void 0:e._$AO)&&r.call(e,!1),void 0===o?e=void 0:(e=new o(t))._$AT(t,n,s),void 0!==s?(null!=(r=n._$Co)?r:n._$Co=[])[s]=e:n._$Cl=e),void 0!==e&&(i=m(t,e._$AS(t,i.values),e,s))}return i}class fe{constructor(e,t){this._$AV=[],this._$AN=void 0,this._$AD=e,this._$AM=t}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}u(t){var{el:{content:e},parts:i}=this._$AD,n=(null!=(n=null==t?void 0:t.creationScope)?n:l).importNode(e,!0);y.currentNode=n;let s=y.nextNode(),r=0,o=0,a=i[0];for(;void 0!==a;){if(r===a.index){let e;2===a.type?e=new ve(s,s.nextSibling,this,t):1===a.type?e=new a.ctor(s,a.name,a.strings,this,t):6===a.type&&(e=new Ee(s,this,t)),this._$AV.push(e),a=i[++o]}r!==(null==a?void 0:a.index)&&(s=y.nextNode(),r++)}return y.currentNode=l,n}v(e){let t=0;for(var i of this._$AV)void 0!==i&&(void 0!==i.strings?(i._$AI(e,i,t),t+=i.strings.length-2):i._$AI(e[t])),t++}}class ve{constructor(e,t,i,n){this.type=2,this._$AH=v,this._$AN=void 0,this._$AA=e,this._$AB=t,this._$AM=i,this.options=n,this._$Cp=null==(e=null==n?void 0:n.isConnected)||e}get _$AU(){var e;return null!=(e=null==(e=this._$AM)?void 0:e._$AU)?e:this._$Cp}get parentNode(){let e=this._$AA.parentNode;var t=this._$AM;return e=void 0!==t&&11===(null==e?void 0:e.nodeType)?t.parentNode:e}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(e,t=this){e=m(this,e,t),d(e)?e===v||null==e||""===e?(this._$AH!==v&&this._$AR(),this._$AH=v):e!==this._$AH&&e!==f&&this._(e):void 0!==e._$litType$?this.g(e):void 0!==e.nodeType?this.$(e):se(e)?this.T(e):this._(e)}k(e){return this._$AA.parentNode.insertBefore(e,this._$AB)}$(e){this._$AH!==e&&(this._$AR(),this._$AH=this.k(e))}_(e){this._$AH!==v&&d(this._$AH)?this._$AA.nextSibling.data=e:this.$(l.createTextNode(e)),this._$AH=e}g(e){var t,{values:i,_$litType$:n}=e,n="number"==typeof n?this._$AC(e):(void 0===n.el&&(n.el=_e.createElement(pe(n.h,n.h[0]),this.options)),n);if((null==(t=this._$AH)?void 0:t._$AD)===n)this._$AH.v(i);else{let e=new fe(n,this),t=e.u(this.options);e.v(i),this.$(t),this._$AH=e}}_$AC(e){let t=de.get(e.strings);return void 0===t&&de.set(e.strings,t=new _e(e)),t}T(e){ne(this._$AH)||(this._$AH=[],this._$AR());var t,i=this._$AH;let n,s=0;for(t of e)s===i.length?i.push(n=new ve(this.k(h()),this.k(h()),this,this.options)):n=i[s],n._$AI(t),s++;s<i.length&&(this._$AR(n&&n._$AB.nextSibling,s),i.length=s)}_$AR(t=this._$AA.nextSibling,e){var i;for(null!=(i=this._$AP)&&i.call(this,!1,!0,e);t&&t!==this._$AB;){let e=t.nextSibling;t.remove(),t=e}}setConnected(e){var t;void 0===this._$AM&&(this._$Cp=e,null!=(t=this._$AP))&&t.call(this,e)}}class ye{constructor(e,t,i,n,s){this.type=1,this._$AH=v,this._$AN=void 0,this.element=e,this.name=t,this._$AM=n,this.options=s,2<i.length||""!==i[0]||""!==i[1]?(this._$AH=Array(i.length-1).fill(new String),this.strings=i):this._$AH=v}get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}_$AI(n,s=this,r,e){var o=this.strings;let a=!1;if(void 0===o)n=m(this,n,s,0),(a=!d(n)||n!==this._$AH&&n!==f)&&(this._$AH=n);else{let e=n,t,i;for(n=o[0],t=0;t<o.length-1;t++)(i=m(this,e[r+t],s,t))===f&&(i=this._$AH[t]),a=a||!d(i)||i!==this._$AH[t],i===v?n=v:n!==v&&(n+=(null!=i?i:"")+o[t+1]),this._$AH[t]=i}a&&!e&&this.j(n)}j(e){e===v?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,null!=e?e:"")}}class me extends ye{constructor(){super(...arguments),this.type=3}j(e){this.element[this.name]=e===v?void 0:e}}let ge=c?c.emptyScript:"";class $e extends ye{constructor(){super(...arguments),this.type=4}j(e){e&&e!==v?this.element.setAttribute(this.name,ge):this.element.removeAttribute(this.name)}}class be extends ye{constructor(e,t,i,n,s){super(e,t,i,n,s),this.type=5}_$AI(e,t=this){var i,n;(e=null!=(t=m(this,e,t,0))?t:v)!==f&&(t=this._$AH,i=e===v&&t!==v||e.capture!==t.capture||e.once!==t.once||e.passive!==t.passive,n=e!==v&&(t===v||i),i&&this.element.removeEventListener(this.name,this,t),n&&this.element.addEventListener(this.name,this,e),this._$AH=e)}handleEvent(e){var t;"function"==typeof this._$AH?this._$AH.call(null!=(t=null==(t=this.options)?void 0:t.host)?t:this.element,e):this._$AH.handleEvent(e)}}class Ee{constructor(e,t,i){this.element=e,this.type=6,this._$AN=void 0,this._$AM=t,this.options=i}get _$AU(){return this._$AM._$AU}_$AI(e){m(this,e)}}var i={O:"$lit$",P:p,A:te,C:1,M:ue,L:fe,R:se,D:m,I:ve,V:ye,H:$e,N:be,U:me,F:Ee},n=Y.litHtmlPolyfillSupport;null!=n&&n(_e,ve),(null!=(n=Y.litHtmlVersions)?n:Y.litHtmlVersions=[]).push("2.8.0");class s extends t{constructor(){super(...arguments),this.renderOptions={host:this},this._$Do=void 0}createRenderRoot(){var e,t=super.createRenderRoot();return null==(e=this.renderOptions).renderBefore&&(e.renderBefore=t.firstChild),t}update(e){var t=this.render();this.hasUpdated||(this.renderOptions.isConnected=this.isConnected),super.update(e),this._$Do=((e,t,i)=>{var n,s=null!=(s=null==i?void 0:i.renderBefore)?s:t;let r=s._$litPart$;if(void 0===r){let e=null!=(n=null==i?void 0:i.renderBefore)?n:null;s._$litPart$=r=new ve(t.insertBefore(h(),e),e,void 0,null!=i?i:{})}return r._$AI(e),r})(t,this.renderRoot,this.renderOptions)}connectedCallback(){var e;super.connectedCallback(),null!=(e=this._$Do)&&e.setConnected(!0)}disconnectedCallback(){var e;super.disconnectedCallback(),null!=(e=this._$Do)&&e.setConnected(!1)}render(){return f}}s.finalized=!0,s._$litElement$=!0,null!=(n=globalThis.litElementHydrateSupport)&&n.call(globalThis,{LitElement:s});var n=globalThis.litElementPolyfillSupport;null!=n&&n({LitElement:s}),(null!=(n=globalThis.litElementVersions)?n:globalThis.litElementVersions=[]).push("3.3.3");let Ae=s=>e=>{var t,i,n;return"function"!=typeof e?(t=s,{kind:n,elements:i}=e,{kind:n,elements:i,finisher(e){customElements.define(t,e)}}):(n=e,customElements.define(s,n),n)};function o(s){return(e,t)=>{return void 0!==t?void e.constructor.createProperty(t,s):(i=s,"method"!==(n=e).kind||!n.descriptor||"value"in n.descriptor?{kind:"field",key:Symbol(),placement:"own",descriptor:{},originalKey:n.key,initializer(){"function"==typeof n.initializer&&(this[n.key]=n.initializer.call(this))},finisher(e){e.createProperty(n.key,i)}}:{...n,finisher(e){e.createProperty(n.key,i)}});var i,n}}function a(e){return o({...e,state:!0})}null!=(n=window.HTMLSlotElement)&&n.prototype.assignedElements;let we=2,ke=t=>(...e)=>({_$litDirective$:t,values:e});class xe{constructor(e){}get _$AU(){return this._$AM._$AU}_$AT(e,t,i){this._$Ct=e,this._$AM=t,this._$Ci=i}_$AS(e,t){return this.update(e,t)}update(e,t){return this.render(...t)}}let Pe=i["I"],je=e=>void 0===e.strings,Oe=()=>document.createComment(""),Se=(n,e,s)=>{var r,o=n._$AA.parentNode,a=void 0===e?n._$AB:e._$AA;if(void 0===s){let e=o.insertBefore(Oe(),a),t=o.insertBefore(Oe(),a);s=new Pe(e,t,n,n.options)}else{let e=s._$AB.nextSibling,t=s._$AM,i=t!==n;if(i){let e;null!=(r=s._$AQ)&&r.call(s,n),s._$AM=n,void 0!==s._$AP&&(e=n._$AU)!==t._$AU&&s._$AP(e)}if(e!==a||i){let t=s._$AA;for(;t!==e;){let e=t.nextSibling;o.insertBefore(t,a),t=e}}}return s},g=(e,t,i=e)=>(e._$AI(t,i),e),Ce={},Me=(e,t=Ce)=>e._$AH=t,De=e=>{var t;null!=(t=e._$AP)&&t.call(e,!1,!0);let i=e._$AA;for(var n=e._$AB.nextSibling;i!==n;){let e=i.nextSibling;i.remove(),i=e}},Ue=(t,i,n)=>{var s=new Map;for(let e=i;e<=n;e++)s.set(t[e],e);return s},He=ke(class extends xe{constructor(e){if(super(e),e.type!==we)throw Error("repeat() can only be used in text expressions")}ct(t,e,i){let n;void 0===i?i=e:void 0!==e&&(n=e);var s=[],r=[];let o=0;for(let e of t)s[o]=n?n(e,o):o,r[o]=i(e,o),o++;return{values:r,keys:s}}render(e,t,i){return this.ct(e,t,i).values}update(i,[e,t,n]){var s=i._$AH,{values:r,keys:o}=this.ct(e,t,n);if(!Array.isArray(s))return this.ut=o,r;var a=null!=(e=this.ut)?e:this.ut=[],l=[];let c,h,d=0,p=s.length-1,u=0,_=r.length-1;for(;d<=p&&u<=_;)if(null===s[d])d++;else if(null===s[p])p--;else if(a[d]===o[u])l[u]=g(s[d],r[u]),d++,u++;else if(a[p]===o[_])l[_]=g(s[p],r[_]),p--,_--;else if(a[d]===o[_])l[_]=g(s[d],r[_]),Se(i,l[_+1],s[d]),d++,_--;else if(a[p]===o[u])l[u]=g(s[p],r[u]),Se(i,s[d],s[p]),p--,u++;else if(void 0===c&&(c=Ue(o,u,_),h=Ue(a,d,p)),c.has(a[d]))if(c.has(a[p])){let e=h.get(o[u]),t=void 0!==e?s[e]:null;if(null===t){let e=Se(i,s[d]);g(e,r[u]),l[u]=e}else l[u]=g(t,r[u]),Se(i,s[d],t),s[e]=null;u++}else De(s[p]),p--;else De(s[d]),d++;for(;u<=_;){let e=Se(i,l[_+1]);g(e,r[u]),l[u++]=e}for(;d<=p;){let e=s[d++];null!==e&&De(e)}return this.ut=o,Me(i,l),f}}),Te=ke(class extends xe{constructor(e){if(super(e),3!==e.type&&1!==e.type&&4!==e.type)throw Error("The `live` directive is not allowed on child or event bindings");if(!je(e))throw Error("`live` bindings can only contain a single expression")}render(e){return e}update(e,[t]){if(t!==f&&t!==v){var i=e.element,n=e.name;if(3===e.type){if(t===i[n])return f}else if(4===e.type){if(!!t===i.hasAttribute(n))return f}else if(1===e.type&&i.getAttribute(n)===t+"")return f;Me(e)}return t}}),Re=(e,t)=>{var i,n,s=e._$AN;if(void 0===s)return!1;for(let e of s)null!=(n=(i=e)._$AO)&&n.call(i,t,!1),Re(e,t);return!0},Be=e=>{let t,i;for(;void 0!==(t=e._$AM)&&((i=t._$AN).delete(e),e=t,0===(null==i?void 0:i.size)););},Le=i=>{for(let t;t=i._$AM;i=t){let e=t._$AN;if(void 0===e)t._$AN=e=new Set;else if(e.has(i))break;e.add(i),Ne(t)}};function Ie(e){void 0!==this._$AN?(Be(this),this._$AM=e,Le(this)):this._$AM=e}function Ke(e,t=!1,i=0){var n=this._$AH,s=this._$AN;if(void 0!==s&&0!==s.size)if(t)if(Array.isArray(n))for(let e=i;e<n.length;e++)Re(n[e],!1),Be(n[e]);else null!=n&&(Re(n,!1),Be(n));else Re(this,e)}let Ne=e=>{e.type==we&&(null==e._$AP&&(e._$AP=Ke),null==e._$AQ)&&(e._$AQ=Ie)};class ze extends xe{constructor(){super(...arguments),this._$AN=void 0}_$AT(e,t,i){super._$AT(e,t,i),Le(this),this.isConnected=e._$AU}_$AO(e,t=!0){var i;e!==this.isConnected&&((this.isConnected=e)?null!=(i=this.reconnected)&&i.call(this):null!=(i=this.disconnected)&&i.call(this)),t&&(Re(this,e),Be(this))}setValue(e){var t;je(this._$Ct)?this._$Ct._$AI(e,this):((t=[...this._$Ct._$AH])[this._$Ci]=e,this._$Ct._$AI(t,this,0))}disconnected(){}reconnected(){}}let We=()=>new Ve;class Ve{}let qe=new WeakMap,Fe=ke(class extends ze{render(e){return v}update(e,[t]){var i=t!==this.G;return i&&void 0!==this.G&&this.ot(void 0),!i&&this.rt===this.lt||(this.G=t,this.dt=null==(i=e.options)?void 0:i.host,this.ot(this.lt=e.element)),v}ot(t){if("function"==typeof this.G){var i=null!=(i=this.dt)?i:globalThis;let e=qe.get(i);void 0===e&&(e=new WeakMap,qe.set(i,e)),void 0!==e.get(this.G)&&this.G.call(this.dt,void 0),e.set(this.G,t),void 0!==t&&this.G.call(this.dt,t)}else this.G.value=t}get rt(){var e;return"function"==typeof this.G?null==(e=qe.get(null!=(e=this.dt)?e:globalThis))?void 0:e.get(this.G):null==(e=this.G)?void 0:e.value}disconnected(){this.rt===this.lt&&this.ot(void 0)}reconnected(){this.ot(this.lt)}}),Je=ke(class extends xe{constructor(e){if(super(e),1!==e.type||"class"!==e.name||2<(null==(e=e.strings)?void 0:e.length))throw Error("`classMap()` can only be used in the `class` attribute and must be the only part in the attribute.")}render(t){return" "+Object.keys(t).filter(e=>t[e]).join(" ")+" "}update(e,[i]){var t,n;if(void 0===this.it){this.it=new Set,void 0!==e.strings&&(this.nt=new Set(e.strings.join(" ").split(/\s/).filter(e=>""!==e)));for(let e in i)!i[e]||null!=(t=this.nt)&&t.has(e)||this.it.add(e);return this.render(i)}let s=e.element.classList;this.it.forEach(e=>{e in i||(s.remove(e),this.it.delete(e))});for(let t in i){let e=!!i[t];e===this.it.has(t)||null!=(n=this.nt)&&n.has(t)||(e?(s.add(t),this.it.add(t)):(s.remove(t),this.it.delete(t)))}return f}}),Ge="undefined"!=typeof navigator&&0<navigator.userAgent.toLowerCase().indexOf("firefox");function Ze(e,t,i){e.addEventListener?e.addEventListener(t,i,!1):e.attachEvent&&e.attachEvent("on".concat(t),function(){i(window.event)})}function Qe(e,t){for(var i=t.slice(0,t.length-1),n=0;n<i.length;n++)i[n]=e[i[n].toLowerCase()];return i}function Xe(e){for(var t=(e=(e="string"!=typeof e?"":e).replace(/\s/g,"")).split(","),i=t.lastIndexOf("");0<=i;)t[i-1]+=",",t.splice(i,1),i=t.lastIndexOf("");return t}for(var Ye={backspace:8,tab:9,clear:12,enter:13,return:13,esc:27,escape:27,space:32,left:37,up:38,right:39,down:40,del:46,delete:46,ins:45,insert:45,home:36,end:35,pageup:33,pagedown:34,capslock:20,num_0:96,num_1:97,num_2:98,num_3:99,num_4:100,num_5:101,num_6:102,num_7:103,num_8:104,num_9:105,num_multiply:106,num_add:107,num_enter:108,num_subtract:109,num_decimal:110,num_divide:111,"⇪":20,",":188,".":190,"/":191,"`":192,"-":Ge?173:189,"=":Ge?61:187,";":Ge?59:186,"'":222,"[":219,"]":221,"\\":220},$={"⇧":16,shift:16,"⌥":18,alt:18,option:18,"⌃":17,ctrl:17,control:17,"⌘":91,cmd:91,command:91},et={16:"shiftKey",18:"altKey",17:"ctrlKey",91:"metaKey",shiftKey:16,ctrlKey:17,altKey:18,metaKey:91},b={16:!1,18:!1,17:!1,91:!1},E={},tt=1;tt<20;tt++)Ye["f".concat(tt)]=111+tt;var A=[],it="all",nt=[],st=function(e){return Ye[e.toLowerCase()]||$[e.toLowerCase()]||e.toUpperCase().charCodeAt(0)};function rt(e){it=e||"all"}function ot(){return it||"all"}function at(e){var t=e.key,n=e.scope,s=e.method,o=void 0===(e=e.splitKey)?"+":e;Xe(t).forEach(function(e){var r,e=e.split(o),t=e.length,i=e[t-1],i="*"===i?"*":st(i);E[i]&&(n=n||ot(),r=1<t?Qe($,e):[],E[i]=E[i].map(function(e){return s&&e.method!==s||e.scope!==n||!function(e){for(var t=e.length>=r.length?e:r,i=e.length>=r.length?r:e,n=!0,s=0;s<t.length;s++)-1===i.indexOf(t[s])&&(n=!1);return n}(e.mods)?e:{}}))})}function lt(e,t,i){var n;if(t.scope===i||"all"===t.scope){for(var s in n=0<t.mods.length,b)Object.prototype.hasOwnProperty.call(b,s)&&(!b[s]&&-1<t.mods.indexOf(+s)||b[s]&&-1===t.mods.indexOf(+s))&&(n=!1);(0!==t.mods.length||b[16]||b[18]||b[17]||b[91])&&!n&&"*"!==t.shortcut||!1===t.method(e,t)&&(e.preventDefault?e.preventDefault():e.returnValue=!1,e.stopPropagation&&e.stopPropagation(),e.cancelBubble)&&(e.cancelBubble=!0)}}function ct(i){var e=E["*"],t=i.keyCode||i.which||i.charCode;if(w.filter.call(this,i)){if(-1===A.indexOf(t=93!==t&&224!==t?t:91)&&229!==t&&A.push(t),["ctrlKey","altKey","shiftKey","metaKey"].forEach(function(e){var t=et[e];i[e]&&-1===A.indexOf(t)?A.push(t):!i[e]&&-1<A.indexOf(t)?A.splice(A.indexOf(t),1):"metaKey"!==e||!i[e]||3!==A.length||i.ctrlKey||i.shiftKey||i.altKey||(A=A.slice(A.indexOf(t)))}),t in b){for(var n in b[t]=!0,$)$[n]===t&&(w[n]=!0);if(!e)return}for(var s in b)Object.prototype.hasOwnProperty.call(b,s)&&(b[s]=i[et[s]]);i.getModifierState&&(!i.altKey||i.ctrlKey)&&i.getModifierState("AltGraph")&&(-1===A.indexOf(17)&&A.push(17),-1===A.indexOf(18)&&A.push(18),b[17]=!0,b[18]=!0);var r=ot();if(e)for(var o=0;o<e.length;o++)e[o].scope===r&&("keydown"===i.type&&e[o].keydown||"keyup"===i.type&&e[o].keyup)&&lt(i,e[o],r);if(t in E)for(var a=0;a<E[t].length;a++)if(("keydown"===i.type&&E[t][a].keydown||"keyup"===i.type&&E[t][a].keyup)&&E[t][a].key){for(var l=E[t][a],c=l.splitKey,h=l.key.split(c),d=[],p=0;p<h.length;p++)d.push(st(h[p]));d.sort().join("")===A.sort().join("")&&lt(i,l,r)}}}function w(e,t,i){A=[];var n=Xe(e),s=[],r="all",o=document,a=0,l=!1,c=!0,h="+";for(void 0===i&&"function"==typeof t&&(i=t),"[object Object]"===Object.prototype.toString.call(t)&&(t.scope&&(r=t.scope),t.element&&(o=t.element),t.keyup&&(l=t.keyup),void 0!==t.keydown&&(c=t.keydown),"string"==typeof t.splitKey)&&(h=t.splitKey),"string"==typeof t&&(r=t);a<n.length;a++)s=[],1<(e=n[a].split(h)).length&&(s=Qe($,e)),(e="*"===(e=e[e.length-1])?"*":st(e))in E||(E[e]=[]),E[e].push({keyup:l,keydown:c,scope:r,mods:s,shortcut:n[a],method:i,key:n[a],splitKey:h});void 0===o||(t=o,-1<nt.indexOf(t))||!window||(nt.push(o),Ze(o,"keydown",function(e){ct(e)}),Ze(window,"focus",function(){A=[]}),Ze(o,"keyup",function(e){ct(e);var t=e.keyCode||e.which||e.charCode,i=A.indexOf(t);if(0<=i&&A.splice(i,1),e.key&&"meta"===e.key.toLowerCase()&&A.splice(0,A.length),(t=93!==t&&224!==t?t:91)in b)for(var n in b[t]=!1,$)$[n]===t&&(w[n]=!1)}))}var ht,dt,pt={setScope:rt,getScope:ot,deleteScope:function(e,t){var i,n,s;for(s in e=e||ot(),E)if(Object.prototype.hasOwnProperty.call(E,s))for(i=E[s],n=0;n<i.length;)i[n].scope===e?i.splice(n,1):n++;ot()===e&&rt(t||"all")},getPressedKeyCodes:function(){return A.slice(0)},isPressed:function(e){return"string"==typeof e&&(e=st(e)),-1!==A.indexOf(e)},filter:function(e){var e=e.target||e.srcElement,t=e.tagName,i=!0;return i=!e.isContentEditable&&("INPUT"!==t&&"TEXTAREA"!==t&&"SELECT"!==t||e.readOnly)?i:!1},unbind:function(e){if(e){if(Array.isArray(e))e.forEach(function(e){e.key&&at(e)});else if("object"==typeof e)e.key&&at(e);else if("string"==typeof e){for(var t=arguments.length,i=new Array(1<t?t-1:0),n=1;n<t;n++)i[n-1]=arguments[n];var s=i[0],r=i[1];"function"==typeof s&&(r=s,s=""),at({key:e,scope:s,method:r,splitKey:"+"})}}else Object.keys(E).forEach(function(e){return delete E[e]})}};for(ht in pt)Object.prototype.hasOwnProperty.call(pt,ht)&&(w[ht]=pt[ht]);"undefined"!=typeof window&&(dt=window.hotkeys,w.noConflict=function(e){return e&&window.hotkeys===w&&(window.hotkeys=dt),w},window.hotkeys=w);function ut(e,t,i,n){var s,r=arguments.length,o=r<3?t:null===n?n=Object.getOwnPropertyDescriptor(t,i):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)o=Reflect.decorate(e,t,i,n);else for(var a=e.length-1;0<=a;a--)(s=e[a])&&(o=(r<3?s(o):3<r?s(t,i,o):s(t,i))||o);return 3<r&&o&&Object.defineProperty(t,i,o),o}var k=w,n=class extends s{constructor(){super(...arguments),this.placeholder="",this.hideBreadcrumbs=!1,this.breadcrumbHome="Home",this.breadcrumbs=[],this._inputRef=We()}render(){let e="";if(!this.hideBreadcrumbs){var t=[];for(let e of this.breadcrumbs)t.push(r`<button
            tabindex="-1"
            @click=${()=>this.selectParent(e)}
            class="breadcrumb"
          >
            ${e}
          </button>`);e=r`<div class="breadcrumb-list">
        <button
          tabindex="-1"
          @click=${()=>this.selectParent()}
          class="breadcrumb"
        >
          ${this.breadcrumbHome}
        </button>
        ${t}
      </div>`}return r`
      ${e}
      <div part="ninja-input-wrapper" class="search-wrapper">
        <input
          part="ninja-input"
          type="text"
          id="search"
          spellcheck="false"
          autocomplete="off"
          @input="${this._handleInput}"
          ${Fe(this._inputRef)}
          placeholder="${this.placeholder}"
          class="search"
        />
      </div>
    `}setSearch(e){this._inputRef.value&&(this._inputRef.value.value=e)}focusSearch(){requestAnimationFrame(()=>this._inputRef.value.focus())}_handleInput(e){e=e.target;this.dispatchEvent(new CustomEvent("change",{detail:{search:e.value},bubbles:!1,composed:!1}))}selectParent(e){this.dispatchEvent(new CustomEvent("setParent",{detail:{parent:e},bubbles:!0,composed:!0}))}firstUpdated(){this.focusSearch()}_close(){this.dispatchEvent(new CustomEvent("close",{bubbles:!0,composed:!0}))}};n.styles=z`
    :host {
      flex: 1;
      position: relative;
    }
    .search {
      padding: 1.25em;
      flex-grow: 1;
      flex-shrink: 0;
      margin: 0px;
      border: none;
      appearance: none;
      font-size: 1.125em;
      background: transparent;
      caret-color: var(--ninja-accent-color);
      color: var(--ninja-text-color);
      outline: none;
      font-family: var(--ninja-font-family);
    }
    .search::placeholder {
      color: var(--ninja-placeholder-color);
    }
    .breadcrumb-list {
      padding: 1em 4em 0 1em;
      display: flex;
      flex-direction: row;
      align-items: stretch;
      justify-content: flex-start;
      flex: initial;
    }

    .breadcrumb {
      background: var(--ninja-secondary-background-color);
      text-align: center;
      line-height: 1.2em;
      border-radius: var(--ninja-key-border-radius);
      border: 0;
      cursor: pointer;
      padding: 0.1em 0.5em;
      color: var(--ninja-secondary-text-color);
      margin-right: 0.5em;
      outline: none;
      font-family: var(--ninja-font-family);
    }

    .search-wrapper {
      display: flex;
      border-bottom: var(--ninja-separate-border);
    }
  `,ut([o()],n.prototype,"placeholder",void 0),ut([o({type:Boolean})],n.prototype,"hideBreadcrumbs",void 0),ut([o()],n.prototype,"breadcrumbHome",void 0),ut([o({type:Array})],n.prototype,"breadcrumbs",void 0),ut([Ae("ninja-header")],n);class _t extends xe{constructor(e){if(super(e),this.et=v,e.type!==we)throw Error(this.constructor.directiveName+"() can only be used in child bindings")}render(e){if(e===v||null==e)return this.ft=void 0,this.et=e;if(e===f)return e;if("string"!=typeof e)throw Error(this.constructor.directiveName+"() called with a non-string value");return e===this.et?this.ft:(e=[this.et=e],this.ft={_$litType$:this.constructor.resultType,strings:e.raw=e,values:[]})}}_t.directiveName="unsafeHTML",_t.resultType=1;let ft=ke(_t),vt=e(2),yt=window,mt=yt.ShadowRoot&&(void 0===yt.ShadyCSS||yt.ShadyCSS.nativeShadow)&&"adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,gt=Symbol(),$t=new WeakMap;class bt{constructor(e,t,i){if(this._$cssResult$=!0,i!==gt)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=e,this.t=t}get styleSheet(){let e=this.o;var t,i=this.t;return mt&&void 0===e&&(t=void 0!==i&&1===i.length,void 0===(e=t?$t.get(i):e))&&((this.o=e=new CSSStyleSheet).replaceSync(this.cssText),t)&&$t.set(i,e),e}toString(){return this.cssText}}let Et=mt?e=>e:t=>{if(!(t instanceof CSSStyleSheet))return t;{let e="";for(var i of t.cssRules)e+=i.cssText;return t=e,new bt("string"==typeof t?t:t+"",void 0,gt)}},At,wt=window,kt=wt.trustedTypes,xt=kt?kt.emptyScript:"",Pt=wt.reactiveElementPolyfillSupport,jt={toAttribute(e,t){switch(t){case Boolean:e=e?xt:null;break;case Object:case Array:e=null==e?e:JSON.stringify(e)}return e},fromAttribute(e,t){let i=e;switch(t){case Boolean:i=null!==e;break;case Number:i=null===e?null:Number(e);break;case Object:case Array:try{i=JSON.parse(e)}catch(e){i=null}}return i}},Ot=(e,t)=>t!==e&&(t==t||e==e),St={attribute:!0,type:String,converter:jt,reflect:!1,hasChanged:Ot};class x extends HTMLElement{constructor(){super(),this._$Ei=new Map,this.isUpdatePending=!1,this.hasUpdated=!1,this._$El=null,this._$Eu()}static addInitializer(e){var t;this.finalize(),(null!=(t=this.h)?t:this.h=[]).push(e)}static get observedAttributes(){this.finalize();let i=[];return this.elementProperties.forEach((e,t)=>{e=this._$Ep(t,e);void 0!==e&&(this._$Ev.set(e,t),i.push(e))}),i}static createProperty(e,t=St){var i;t.state&&(t.attribute=!1),this.finalize(),this.elementProperties.set(e,t),t.noAccessor||this.prototype.hasOwnProperty(e)||(i="symbol"==typeof e?Symbol():"__"+e,void 0!==(i=this.getPropertyDescriptor(e,i,t))&&Object.defineProperty(this.prototype,e,i))}static getPropertyDescriptor(i,n,s){return{get(){return this[n]},set(e){var t=this[i];this[n]=e,this.requestUpdate(i,t,s)},configurable:!0,enumerable:!0}}static getPropertyOptions(e){return this.elementProperties.get(e)||St}static finalize(){if(this.hasOwnProperty("finalized"))return!1;this.finalized=!0;let e=Object.getPrototypeOf(this);if(e.finalize(),void 0!==e.h&&(this.h=[...e.h]),this.elementProperties=new Map(e.elementProperties),this._$Ev=new Map,this.hasOwnProperty("properties")){let e=this.properties,t=[...Object.getOwnPropertyNames(e),...Object.getOwnPropertySymbols(e)];for(var i of t)this.createProperty(i,e[i])}return this.elementStyles=this.finalizeStyles(this.styles),!0}static finalizeStyles(e){var t=[];if(Array.isArray(e)){var i=new Set(e.flat(1/0).reverse());for(let e of i)t.unshift(Et(e))}else void 0!==e&&t.push(Et(e));return t}static _$Ep(e,t){t=t.attribute;return!1===t?void 0:"string"==typeof t?t:"string"==typeof e?e.toLowerCase():void 0}_$Eu(){var e;this._$E_=new Promise(e=>this.enableUpdating=e),this._$AL=new Map,this._$Eg(),this.requestUpdate(),null!=(e=this.constructor.h)&&e.forEach(e=>e(this))}addController(e){var t;(null!=(t=this._$ES)?t:this._$ES=[]).push(e),void 0!==this.renderRoot&&this.isConnected&&null!=(t=e.hostConnected)&&t.call(e)}removeController(e){var t;null!=(t=this._$ES)&&t.splice(this._$ES.indexOf(e)>>>0,1)}_$Eg(){this.constructor.elementProperties.forEach((e,t)=>{this.hasOwnProperty(t)&&(this._$Ei.set(t,this[t]),delete this[t])})}createRenderRoot(){var n,e,t=null!=(t=this.shadowRoot)?t:this.attachShadow(this.constructor.shadowRootOptions);return n=t,e=this.constructor.elementStyles,mt?n.adoptedStyleSheets=e.map(e=>e instanceof CSSStyleSheet?e:e.styleSheet):e.forEach(e=>{var t=document.createElement("style"),i=yt.litNonce;void 0!==i&&t.setAttribute("nonce",i),t.textContent=e.cssText,n.appendChild(t)}),t}connectedCallback(){var e;void 0===this.renderRoot&&(this.renderRoot=this.createRenderRoot()),this.enableUpdating(!0),null!=(e=this._$ES)&&e.forEach(e=>{var t;return null==(t=e.hostConnected)?void 0:t.call(e)})}enableUpdating(e){}disconnectedCallback(){var e;null!=(e=this._$ES)&&e.forEach(e=>{var t;return null==(t=e.hostDisconnected)?void 0:t.call(e)})}attributeChangedCallback(e,t,i){this._$AK(e,i)}_$EO(e,t,i=St){var n,s=this.constructor._$Ep(e,i);void 0!==s&&!0===i.reflect&&(n=(void 0!==(null==(n=i.converter)?void 0:n.toAttribute)?i.converter:jt).toAttribute(t,i.type),this._$El=e,null==n?this.removeAttribute(s):this.setAttribute(s,n),this._$El=null)}_$AK(e,i){var n=this.constructor,s=n._$Ev.get(e);if(void 0!==s&&this._$El!==s){let e=n.getPropertyOptions(s),t="function"==typeof e.converter?{fromAttribute:e.converter}:void 0!==(null==(n=e.converter)?void 0:n.fromAttribute)?e.converter:jt;this._$El=s,this[s]=t.fromAttribute(i,e.type),this._$El=null}}requestUpdate(e,t,i){let n=!0;void 0!==e&&(((i=i||this.constructor.getPropertyOptions(e)).hasChanged||Ot)(this[e],t)?(this._$AL.has(e)||this._$AL.set(e,t),!0===i.reflect&&this._$El!==e&&(void 0===this._$EC&&(this._$EC=new Map),this._$EC.set(e,i))):n=!1),!this.isUpdatePending&&n&&(this._$E_=this._$Ej())}async _$Ej(){this.isUpdatePending=!0;try{await this._$E_}catch(e){Promise.reject(e)}var e=this.scheduleUpdate();return null!=e&&await e,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){var t;if(this.isUpdatePending){this.hasUpdated,this._$Ei&&(this._$Ei.forEach((e,t)=>this[t]=e),this._$Ei=void 0);let e=!1;var i=this._$AL;try{(e=this.shouldUpdate(i))?(this.willUpdate(i),null!=(t=this._$ES)&&t.forEach(e=>{var t;return null==(t=e.hostUpdate)?void 0:t.call(e)}),this.update(i)):this._$Ek()}catch(t){throw e=!1,this._$Ek(),t}e&&this._$AE(i)}}willUpdate(e){}_$AE(e){var t;null!=(t=this._$ES)&&t.forEach(e=>{var t;return null==(t=e.hostUpdated)?void 0:t.call(e)}),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(e)),this.updated(e)}_$Ek(){this._$AL=new Map,this.isUpdatePending=!1}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$E_}shouldUpdate(e){return!0}update(e){void 0!==this._$EC&&(this._$EC.forEach((e,t)=>this._$EO(t,this[t],e)),this._$EC=void 0),this._$Ek()}updated(e){}firstUpdated(e){}}x.finalized=!0,x.elementProperties=new Map,x.elementStyles=[],x.shadowRootOptions={mode:"open"},null!=Pt&&Pt({ReactiveElement:x}),(null!=(At=wt.reactiveElementVersions)?At:wt.reactiveElementVersions=[]).push("1.6.3");let Ct=window,P=Ct.trustedTypes,Mt=P?P.createPolicy("lit-html",{createHTML:e=>e}):void 0,j=`lit$${(Math.random()+"").slice(9)}$`,Dt="?"+j,Ut=`<${Dt}>`,O=document,Ht=()=>O.createComment(""),Tt=e=>null===e||"object"!=typeof e&&"function"!=typeof e,Rt=Array.isArray,Bt=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,Lt=/-->/g,It=/>/g,S=RegExp(">|[ \t\n\f\r](?:([^\\s\"'>=/]+)([ \t\n\f\r]*=[ \t\n\f\r]*(?:[^ \t\n\f\r\"'`<>=]|(\"|')|))|$)","g"),Kt=/'/g,Nt=/"/g,zt=/^(?:script|style|textarea|title)$/i,Wt=i=>(e,...t)=>({_$litType$:i,strings:e,values:t}),Vt=Wt(1),C=(Wt(2),Symbol.for("lit-noChange")),M=Symbol.for("lit-nothing"),qt=new WeakMap,D=O.createTreeWalker(O,129,null,!1);function Ft(e,t){if(Array.isArray(e)&&e.hasOwnProperty("raw"))return void 0!==Mt?Mt.createHTML(t):t;throw Error("invalid template strings array")}class Jt{constructor({strings:e,_$litType$:t},i){var n;this.parts=[];let s=0,r=0;var o=e.length-1,a=this.parts,[e,l]=((o,e)=>{let t=o.length-1,a=[],l,c=2===e?"<svg>":"",h=Bt;for(let r=0;r<t;r++){let e=o[r],t,i,n=-1,s=0;for(;s<e.length&&(h.lastIndex=s,null!==(i=h.exec(e)));)s=h.lastIndex,h===Bt?"!--"===i[1]?h=Lt:void 0!==i[1]?h=It:void 0!==i[2]?(zt.test(i[2])&&(l=RegExp("</"+i[2],"g")),h=S):void 0!==i[3]&&(h=S):h===S?">"===i[0]?(h=null!=l?l:Bt,n=-1):void 0===i[1]?n=-2:(n=h.lastIndex-i[2].length,t=i[1],h=void 0===i[3]?S:'"'===i[3]?Nt:Kt):h===Nt||h===Kt?h=S:h===Lt||h===It?h=Bt:(h=S,l=void 0);var d=h===S&&o[r+1].startsWith("/>")?" ":"";c+=h===Bt?e+Ut:0<=n?(a.push(t),e.slice(0,n)+"$lit$"+e.slice(n)+j+d):e+j+(-2===n?(a.push(void 0),r):d)}return[Ft(o,c+(o[t]||"<?>")+(2===e?"</svg>":"")),a]})(e,t);if(this.el=Jt.createElement(e,i),D.currentNode=this.el.content,2===t){let e=this.el.content,t=e.firstChild;t.remove(),e.append(...t.childNodes)}for(;null!==(n=D.nextNode())&&a.length<o;){if(1===n.nodeType){if(n.hasAttributes()){let t=[];for(let e of n.getAttributeNames())if(e.endsWith("$lit$")||e.startsWith(j)){let i=l[r++];if(t.push(e),void 0!==i){let e=n.getAttribute(i.toLowerCase()+"$lit$").split(j),t=/([.?@])?(.*)/.exec(i);a.push({type:1,index:s,name:t[2],strings:e,ctor:"."===t[1]?Xt:"?"===t[1]?ei:"@"===t[1]?ti:Qt})}else a.push({type:6,index:s})}for(let e of t)n.removeAttribute(e)}if(zt.test(n.tagName)){let t=n.textContent.split(j),i=t.length-1;if(0<i){n.textContent=P?P.emptyScript:"";for(let e=0;e<i;e++)n.append(t[e],Ht()),D.nextNode(),a.push({type:2,index:++s});n.append(t[i],Ht())}}}else if(8===n.nodeType)if(n.data===Dt)a.push({type:2,index:s});else{let e=-1;for(;-1!==(e=n.data.indexOf(j,e+1));)a.push({type:7,index:s}),e+=j.length-1}s++}}static createElement(e,t){var i=O.createElement("template");return i.innerHTML=e,i}}function U(t,i,n=t,s){var r;if(i!==C){let e=void 0!==s?null==(o=n._$Co)?void 0:o[s]:n._$Cl;var o=Tt(i)?void 0:i._$litDirective$;(null==e?void 0:e.constructor)!==o&&(null!=(r=null==e?void 0:e._$AO)&&r.call(e,!1),void 0===o?e=void 0:(e=new o(t))._$AT(t,n,s),void 0!==s?(null!=(r=n._$Co)?r:n._$Co=[])[s]=e:n._$Cl=e),void 0!==e&&(i=U(t,e._$AS(t,i.values),e,s))}return i}class Gt{constructor(e,t){this._$AV=[],this._$AN=void 0,this._$AD=e,this._$AM=t}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}u(t){var{el:{content:e},parts:i}=this._$AD,n=(null!=(n=null==t?void 0:t.creationScope)?n:O).importNode(e,!0);D.currentNode=n;let s=D.nextNode(),r=0,o=0,a=i[0];for(;void 0!==a;){if(r===a.index){let e;2===a.type?e=new Zt(s,s.nextSibling,this,t):1===a.type?e=new a.ctor(s,a.name,a.strings,this,t):6===a.type&&(e=new ii(s,this,t)),this._$AV.push(e),a=i[++o]}r!==(null==a?void 0:a.index)&&(s=D.nextNode(),r++)}return D.currentNode=O,n}v(e){let t=0;for(var i of this._$AV)void 0!==i&&(void 0!==i.strings?(i._$AI(e,i,t),t+=i.strings.length-2):i._$AI(e[t])),t++}}class Zt{constructor(e,t,i,n){this.type=2,this._$AH=M,this._$AN=void 0,this._$AA=e,this._$AB=t,this._$AM=i,this.options=n,this._$Cp=null==(e=null==n?void 0:n.isConnected)||e}get _$AU(){var e;return null!=(e=null==(e=this._$AM)?void 0:e._$AU)?e:this._$Cp}get parentNode(){let e=this._$AA.parentNode;var t=this._$AM;return e=void 0!==t&&11===(null==e?void 0:e.nodeType)?t.parentNode:e}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(e,t=this){e=U(this,e,t),Tt(e)?e===M||null==e||""===e?(this._$AH!==M&&this._$AR(),this._$AH=M):e!==this._$AH&&e!==C&&this._(e):void 0!==e._$litType$?this.g(e):void 0!==e.nodeType?this.$(e):(t=e,Rt(t)||"function"==typeof(null==t?void 0:t[Symbol.iterator])?this.T(e):this._(e))}k(e){return this._$AA.parentNode.insertBefore(e,this._$AB)}$(e){this._$AH!==e&&(this._$AR(),this._$AH=this.k(e))}_(e){this._$AH!==M&&Tt(this._$AH)?this._$AA.nextSibling.data=e:this.$(O.createTextNode(e)),this._$AH=e}g(e){var t,{values:i,_$litType$:n}=e,n="number"==typeof n?this._$AC(e):(void 0===n.el&&(n.el=Jt.createElement(Ft(n.h,n.h[0]),this.options)),n);if((null==(t=this._$AH)?void 0:t._$AD)===n)this._$AH.v(i);else{let e=new Gt(n,this),t=e.u(this.options);e.v(i),this.$(t),this._$AH=e}}_$AC(e){let t=qt.get(e.strings);return void 0===t&&qt.set(e.strings,t=new Jt(e)),t}T(e){Rt(this._$AH)||(this._$AH=[],this._$AR());var t,i=this._$AH;let n,s=0;for(t of e)s===i.length?i.push(n=new Zt(this.k(Ht()),this.k(Ht()),this,this.options)):n=i[s],n._$AI(t),s++;s<i.length&&(this._$AR(n&&n._$AB.nextSibling,s),i.length=s)}_$AR(t=this._$AA.nextSibling,e){var i;for(null!=(i=this._$AP)&&i.call(this,!1,!0,e);t&&t!==this._$AB;){let e=t.nextSibling;t.remove(),t=e}}setConnected(e){var t;void 0===this._$AM&&(this._$Cp=e,null!=(t=this._$AP))&&t.call(this,e)}}class Qt{constructor(e,t,i,n,s){this.type=1,this._$AH=M,this._$AN=void 0,this.element=e,this.name=t,this._$AM=n,this.options=s,2<i.length||""!==i[0]||""!==i[1]?(this._$AH=Array(i.length-1).fill(new String),this.strings=i):this._$AH=M}get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}_$AI(n,s=this,r,e){var o=this.strings;let a=!1;if(void 0===o)n=U(this,n,s,0),(a=!Tt(n)||n!==this._$AH&&n!==C)&&(this._$AH=n);else{let e=n,t,i;for(n=o[0],t=0;t<o.length-1;t++)(i=U(this,e[r+t],s,t))===C&&(i=this._$AH[t]),a=a||!Tt(i)||i!==this._$AH[t],i===M?n=M:n!==M&&(n+=(null!=i?i:"")+o[t+1]),this._$AH[t]=i}a&&!e&&this.j(n)}j(e){e===M?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,null!=e?e:"")}}class Xt extends Qt{constructor(){super(...arguments),this.type=3}j(e){this.element[this.name]=e===M?void 0:e}}let Yt=P?P.emptyScript:"";class ei extends Qt{constructor(){super(...arguments),this.type=4}j(e){e&&e!==M?this.element.setAttribute(this.name,Yt):this.element.removeAttribute(this.name)}}class ti extends Qt{constructor(e,t,i,n,s){super(e,t,i,n,s),this.type=5}_$AI(e,t=this){var i,n;(e=null!=(t=U(this,e,t,0))?t:M)!==C&&(t=this._$AH,i=e===M&&t!==M||e.capture!==t.capture||e.once!==t.once||e.passive!==t.passive,n=e!==M&&(t===M||i),i&&this.element.removeEventListener(this.name,this,t),n&&this.element.addEventListener(this.name,this,e),this._$AH=e)}handleEvent(e){var t;"function"==typeof this._$AH?this._$AH.call(null!=(t=null==(t=this.options)?void 0:t.host)?t:this.element,e):this._$AH.handleEvent(e)}}class ii{constructor(e,t,i){this.element=e,this.type=6,this._$AN=void 0,this._$AM=t,this.options=i}get _$AU(){return this._$AM._$AU}_$AI(e){U(this,e)}}i=Ct.litHtmlPolyfillSupport;null!=i&&i(Jt,Zt),(null!=(n=Ct.litHtmlVersions)?n:Ct.litHtmlVersions=[]).push("2.8.0");class ni extends x{constructor(){super(...arguments),this.renderOptions={host:this},this._$Do=void 0}createRenderRoot(){var e,t=super.createRenderRoot();return null==(e=this.renderOptions).renderBefore&&(e.renderBefore=t.firstChild),t}update(e){var t=this.render();this.hasUpdated||(this.renderOptions.isConnected=this.isConnected),super.update(e),this._$Do=((e,t,i)=>{var n,s=null!=(s=null==i?void 0:i.renderBefore)?s:t;let r=s._$litPart$;if(void 0===r){let e=null!=(n=null==i?void 0:i.renderBefore)?n:null;s._$litPart$=r=new Zt(t.insertBefore(Ht(),e),e,void 0,null!=i?i:{})}return r._$AI(e),r})(t,this.renderRoot,this.renderOptions)}connectedCallback(){var e;super.connectedCallback(),null!=(e=this._$Do)&&e.setConnected(!0)}disconnectedCallback(){var e;super.disconnectedCallback(),null!=(e=this._$Do)&&e.setConnected(!1)}render(){return C}}ni.finalized=!0,ni._$litElement$=!0,null!=(e=globalThis.litElementHydrateSupport)&&e.call(globalThis,{LitElement:ni});function si(e,t,i,n){var s,r=arguments.length,o=r<3?t:null===n?n=Object.getOwnPropertyDescriptor(t,i):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)o=Reflect.decorate(e,t,i,n);else for(var a=e.length-1;0<=a;a--)(s=e[a])&&(o=(r<3?s(o):3<r?s(t,i,o):s(t,i))||o);return 3<r&&o&&Object.defineProperty(t,i,o),o}i=globalThis.litElementPolyfillSupport,null!=i&&i({LitElement:ni}),(null!=(n=globalThis.litElementVersions)?n:globalThis.litElementVersions=[]).push("3.3.3"),null!=(e=window.HTMLSlotElement)&&e.prototype.assignedElements,i=((n,...e)=>{e=1===n.length?n[0]:e.reduce((e,t,i)=>e+(()=>{if(!0===t._$cssResult$)return t.cssText;if("number"==typeof t)return t;throw Error("Value passed to 'css' function must be a 'css' function result: "+t+". Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.")})()+n[i+1],n[0]);return new bt(e,n,gt)})`:host{font-family:var(--mdc-icon-font, "Material Icons");font-weight:normal;font-style:normal;font-size:var(--mdc-icon-size, 24px);line-height:1;letter-spacing:normal;text-transform:none;display:inline-block;white-space:nowrap;word-wrap:normal;direction:ltr;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;-moz-osx-font-smoothing:grayscale;font-feature-settings:"liga"}`,n=class extends ni{render(){return Vt`<span><slot></slot></span>`}},n.styles=[i],Object(vt.c)([e=>{var t,i;return"function"!=typeof e?({kind:i,elements:t}=e,{kind:i,elements:t,finisher(e){customElements.define("mwc-icon",e)}}):(i=e,customElements.define("mwc-icon",i),i)}],n),e=class extends s{constructor(){super(),this.selected=!1,this.hotKeysJoinedView=!0,this.addEventListener("click",this.click)}ensureInView(){requestAnimationFrame(()=>this.scrollIntoView({block:"nearest"}))}click(){this.dispatchEvent(new CustomEvent("actionsSelected",{detail:this.action,bubbles:!0,composed:!0}))}updated(e){e.has("selected")&&this.selected&&this.ensureInView()}render(){let e,t;this.action.mdIcon?e=r`<mwc-icon part="ninja-icon" class="ninja-icon"
        >${this.action.mdIcon}</mwc-icon
      >`:this.action.icon&&(e=ft(this.action.icon||"")),this.action.hotkey&&(t=this.hotKeysJoinedView?this.action.hotkey.split(",").map(e=>{e=e.split("+"),e=r`${function*(t){if(void 0!==t){let e=-1;for(var i of t)-1<e&&(yield"+"),e++,yield i}}(e.map(e=>r`<kbd>${e}</kbd>`))}`;return r`<div class="ninja-hotkey ninja-hotkeys">
            ${e}
          </div>`}):this.action.hotkey.split(",").map(e=>{e=e.split("+").map(e=>r`<kbd class="ninja-hotkey">${e}</kbd>`);return r`<kbd class="ninja-hotkeys">${e}</kbd>`}));var i={selected:this.selected,"ninja-action":!0};return r`
      <div
        class="ninja-action"
        part="ninja-action ${this.selected?"ninja-selected":""}"
        class=${Je(i)}
      >
        ${e}
        <div class="ninja-title">${this.action.title}</div>
        ${t}
      </div>
    `}};e.styles=z`
    :host {
      display: flex;
      width: 100%;
    }
    .ninja-action {
      padding: 0.75em 1em;
      display: flex;
      border-left: 2px solid transparent;
      align-items: center;
      justify-content: start;
      outline: none;
      transition: color 0s ease 0s;
      width: 100%;
    }
    .ninja-action.selected {
      cursor: pointer;
      color: var(--ninja-selected-text-color);
      background-color: var(--ninja-selected-background);
      border-left: 2px solid var(--ninja-accent-color);
      outline: none;
    }
    .ninja-action.selected .ninja-icon {
      color: var(--ninja-selected-text-color);
    }
    .ninja-icon {
      font-size: var(--ninja-icon-size);
      max-width: var(--ninja-icon-size);
      max-height: var(--ninja-icon-size);
      margin-right: 1em;
      color: var(--ninja-icon-color);
      margin-right: 1em;
      position: relative;
    }

    .ninja-title {
      flex-shrink: 0.01;
      margin-right: 0.5em;
      flex-grow: 1;
      font-size: 0.8125em;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .ninja-hotkeys {
      flex-shrink: 0;
      width: min-content;
      display: flex;
    }

    .ninja-hotkeys kbd {
      font-family: inherit;
    }
    .ninja-hotkey {
      background: var(--ninja-secondary-background-color);
      padding: 0.06em 0.25em;
      border-radius: var(--ninja-key-border-radius);
      text-transform: capitalize;
      color: var(--ninja-secondary-text-color);
      font-size: 0.75em;
      font-family: inherit;
    }

    .ninja-hotkey + .ninja-hotkey {
      margin-left: 0.5em;
    }
    .ninja-hotkeys + .ninja-hotkeys {
      margin-left: 1em;
    }
  `,si([o({type:Object})],e.prototype,"action",void 0),si([o({type:Boolean})],e.prototype,"selected",void 0),si([o({type:Boolean})],e.prototype,"hotKeysJoinedView",void 0),si([Ae("ninja-action")],e);function H(e,t,i,n){var s,r=arguments.length,o=r<3?t:null===n?n=Object.getOwnPropertyDescriptor(t,i):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)o=Reflect.decorate(e,t,i,n);else for(var a=e.length-1;0<=a;a--)(s=e[a])&&(o=(r<3?s(o):3<r?s(t,i,o):s(t,i))||o);return 3<r&&o&&Object.defineProperty(t,i,o),o}let ri=r` <div class="modal-footer" slot="footer">
  <span class="help">
    <svg
      version="1.0"
      class="ninja-examplekey"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 1280 1280"
    >
      <path
        d="M1013 376c0 73.4-.4 113.3-1.1 120.2a159.9 159.9 0 0 1-90.2 127.3c-20 9.6-36.7 14-59.2 15.5-7.1.5-121.9.9-255 1h-242l95.5-95.5 95.5-95.5-38.3-38.2-38.2-38.3-160 160c-88 88-160 160.4-160 161 0 .6 72 73 160 161l160 160 38.2-38.3 38.3-38.2-95.5-95.5-95.5-95.5h251.1c252.9 0 259.8-.1 281.4-3.6 72.1-11.8 136.9-54.1 178.5-116.4 8.6-12.9 22.6-40.5 28-55.4 4.4-12 10.7-36.1 13.1-50.6 1.6-9.6 1.8-21 2.1-132.8l.4-122.2H1013v110z"
      />
    </svg>

    to select
  </span>
  <span class="help">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="ninja-examplekey"
      viewBox="0 0 24 24"
    >
      <path d="M0 0h24v24H0V0z" fill="none" />
      <path
        d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"
      />
    </svg>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="ninja-examplekey"
      viewBox="0 0 24 24"
    >
      <path d="M0 0h24v24H0V0z" fill="none" />
      <path d="M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z" />
    </svg>
    to navigate
  </span>
  <span class="help">
    <span class="ninja-examplekey esc">esc</span>
    to close
  </span>
  <span class="help">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="ninja-examplekey backspace"
      viewBox="0 0 20 20"
      fill="currentColor"
    >
      <path
        fill-rule="evenodd"
        d="M6.707 4.879A3 3 0 018.828 4H15a3 3 0 013 3v6a3 3 0 01-3 3H8.828a3 3 0 01-2.12-.879l-4.415-4.414a1 1 0 010-1.414l4.414-4.414zm4 2.414a1 1 0 00-1.414 1.414L10.586 10l-1.293 1.293a1 1 0 101.414 1.414L12 11.414l1.293 1.293a1 1 0 001.414-1.414L13.414 10l1.293-1.293a1 1 0 00-1.414-1.414L12 8.586l-1.293-1.293z"
        clip-rule="evenodd"
      />
    </svg>
    move to parent
  </span>
</div>`,oi=z`
  :host {
    --ninja-width: 640px;
    --ninja-backdrop-filter: none;
    --ninja-overflow-background: rgba(255, 255, 255, 0.5);
    --ninja-text-color: rgb(60, 65, 73);
    --ninja-font-size: 16px;
    --ninja-top: 20%;

    --ninja-key-border-radius: 0.25em;
    --ninja-accent-color: rgb(110, 94, 210);
    --ninja-secondary-background-color: rgb(239, 241, 244);
    --ninja-secondary-text-color: rgb(107, 111, 118);

    --ninja-selected-background: rgb(248, 249, 251);

    --ninja-icon-color: var(--ninja-secondary-text-color);
    --ninja-icon-size: 1.2em;
    --ninja-separate-border: 1px solid var(--ninja-secondary-background-color);

    --ninja-modal-background: #fff;
    --ninja-modal-shadow: rgb(0 0 0 / 50%) 0px 16px 70px;

    --ninja-actions-height: 300px;
    --ninja-group-text-color: rgb(144, 149, 157);

    --ninja-footer-background: rgba(242, 242, 242, 0.4);

    --ninja-placeholder-color: #8e8e8e;

    font-size: var(--ninja-font-size);

    --ninja-z-index: 1;
  }

  :host(.dark) {
    --ninja-backdrop-filter: none;
    --ninja-overflow-background: rgba(0, 0, 0, 0.7);
    --ninja-text-color: #7d7d7d;

    --ninja-modal-background: rgba(17, 17, 17, 0.85);
    --ninja-accent-color: rgb(110, 94, 210);
    --ninja-secondary-background-color: rgba(51, 51, 51, 0.44);
    --ninja-secondary-text-color: #888;

    --ninja-selected-text-color: #eaeaea;
    --ninja-selected-background: rgba(51, 51, 51, 0.44);

    --ninja-icon-color: var(--ninja-secondary-text-color);
    --ninja-separate-border: 1px solid var(--ninja-secondary-background-color);

    --ninja-modal-shadow: 0 16px 70px rgba(0, 0, 0, 0.2);

    --ninja-group-text-color: rgb(144, 149, 157);

    --ninja-footer-background: rgba(30, 30, 30, 85%);
  }

  .modal {
    display: none;
    position: fixed;
    z-index: var(--ninja-z-index);
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background: var(--ninja-overflow-background);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    -webkit-backdrop-filter: var(--ninja-backdrop-filter);
    backdrop-filter: var(--ninja-backdrop-filter);
    text-align: left;
    color: var(--ninja-text-color);
    font-family: var(--ninja-font-family);
  }
  .modal.visible {
    display: block;
  }

  .modal-content {
    position: relative;
    top: var(--ninja-top);
    margin: auto;
    padding: 0;
    display: flex;
    flex-direction: column;
    flex-shrink: 1;
    -webkit-box-flex: 1;
    flex-grow: 1;
    min-width: 0px;
    will-change: transform;
    background: var(--ninja-modal-background);
    border-radius: 0.5em;
    box-shadow: var(--ninja-modal-shadow);
    max-width: var(--ninja-width);
    overflow: hidden;
  }

  .bump {
    animation: zoom-in-zoom-out 0.2s ease;
  }

  @keyframes zoom-in-zoom-out {
    0% {
      transform: scale(0.99);
    }
    50% {
      transform: scale(1.01, 1.01);
    }
    100% {
      transform: scale(1, 1);
    }
  }

  .ninja-github {
    color: var(--ninja-keys-text-color);
    font-weight: normal;
    text-decoration: none;
  }

  .actions-list {
    max-height: var(--ninja-actions-height);
    overflow: auto;
    scroll-behavior: smooth;
    position: relative;
    margin: 0;
    padding: 0.5em 0;
    list-style: none;
    scroll-behavior: smooth;
  }

  .group-header {
    height: 1.375em;
    line-height: 1.375em;
    padding-left: 1.25em;
    padding-top: 0.5em;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    font-size: 0.75em;
    line-height: 1em;
    color: var(--ninja-group-text-color);
    margin: 1px 0;
  }

  .modal-footer {
    background: var(--ninja-footer-background);
    padding: 0.5em 1em;
    display: flex;
    /* font-size: 0.75em; */
    border-top: var(--ninja-separate-border);
    color: var(--ninja-secondary-text-color);
  }

  .modal-footer .help {
    display: flex;
    margin-right: 1em;
    align-items: center;
    font-size: 0.75em;
  }

  .ninja-examplekey {
    background: var(--ninja-secondary-background-color);
    padding: 0.06em 0.25em;
    border-radius: var(--ninja-key-border-radius);
    color: var(--ninja-secondary-text-color);
    width: 1em;
    height: 1em;
    margin-right: 0.5em;
    font-size: 1.25em;
    fill: currentColor;
  }
  .ninja-examplekey.esc {
    width: auto;
    height: auto;
    font-size: 1.1em;
  }
  .ninja-examplekey.backspace {
    opacity: 0.7;
  }
`;i=class extends s{constructor(){super(...arguments),this.placeholder="Type a command or search...",this.disableHotkeys=!1,this.hideBreadcrumbs=!1,this.openHotkey="cmd+k,ctrl+k",this.navigationUpHotkey="up,shift+tab",this.navigationDownHotkey="down,tab",this.closeHotkey="esc",this.goBackHotkey="backspace",this.selectHotkey="enter",this.hotKeysJoinedView=!1,this.noAutoLoadMdIcons=!1,this.data=[],this.visible=!1,this._bump=!0,this._actionMatches=[],this._search="",this._flatData=[],this._headerRef=We()}open(e={}){this._bump=!0,this.visible=!0,this._headerRef.value.focusSearch(),0<this._actionMatches.length&&(this._selected=this._actionMatches[0]),this.setParent(e.parent)}close(){this._bump=!1,this.visible=!1}setParent(e){this._currentRoot=e||void 0,this._selected=void 0,this._search="",this._headerRef.value.setSearch("")}get breadcrumbs(){var e,t=[];let i=null==(e=this._selected)?void 0:e.parent;if(i)for(t.push(i);i;){let e=this._flatData.find(e=>e.id===i);null!=e&&e.parent&&t.push(e.parent),i=e?e.parent:void 0}return t.reverse()}connectedCallback(){super.connectedCallback(),this.noAutoLoadMdIcons||document.fonts.load("24px Material Icons","apps").then(()=>{}),this._registerInternalHotkeys()}disconnectedCallback(){super.disconnectedCallback(),this._unregisterInternalHotkeys()}_flattern(e,n){let s=[];return(e=e||[]).map(e=>{var t=e.children&&e.children.some(e=>"string"==typeof e),i={...e,parent:e.parent||n};return t||(i.children&&i.children.length&&(n=e.id,s=[...s,...i.children]),i.children=i.children?i.children.map(e=>e.id):[]),i}).concat(s.length?this._flattern(s,n):s)}update(e){e.has("data")&&!this.disableHotkeys&&(this._flatData=this._flattern(this.data),this._flatData.filter(e=>!!e.hotkey).forEach(t=>{k(t.hotkey,e=>{e.preventDefault(),t.handler&&t.handler(t)})})),super.update(e)}_registerInternalHotkeys(){this.openHotkey&&k(this.openHotkey,e=>{e.preventDefault(),this.visible?this.close():this.open()}),this.selectHotkey&&k(this.selectHotkey,e=>{this.visible&&(e.preventDefault(),this._actionSelected(this._actionMatches[this._selectedIndex]))}),this.goBackHotkey&&k(this.goBackHotkey,e=>{!this.visible||this._search||(e.preventDefault(),this._goBack())}),this.navigationDownHotkey&&k(this.navigationDownHotkey,e=>{this.visible&&(e.preventDefault(),this._selectedIndex>=this._actionMatches.length-1?this._selected=this._actionMatches[0]:this._selected=this._actionMatches[this._selectedIndex+1])}),this.navigationUpHotkey&&k(this.navigationUpHotkey,e=>{this.visible&&(e.preventDefault(),0===this._selectedIndex?this._selected=this._actionMatches[this._actionMatches.length-1]:this._selected=this._actionMatches[this._selectedIndex-1])}),this.closeHotkey&&k(this.closeHotkey,()=>{this.visible&&this.close()})}_unregisterInternalHotkeys(){this.openHotkey&&k.unbind(this.openHotkey),this.selectHotkey&&k.unbind(this.selectHotkey),this.goBackHotkey&&k.unbind(this.goBackHotkey),this.navigationDownHotkey&&k.unbind(this.navigationDownHotkey),this.navigationUpHotkey&&k.unbind(this.navigationUpHotkey),this.closeHotkey&&k.unbind(this.closeHotkey)}_actionFocused(e,t){this._selected=e,t.target.ensureInView()}_onTransitionEnd(){this._bump=!1}_goBack(){var e=1<this.breadcrumbs.length?this.breadcrumbs[this.breadcrumbs.length-2]:void 0;this.setParent(e)}render(){var e={bump:this._bump,"modal-content":!0},t={visible:this.visible,modal:!0},i=this._flatData.filter(e=>{var t=new RegExp(this._search,"gi"),i=e.title.match(t)||(null==(i=e.keywords)?void 0:i.match(t));return(!this._currentRoot&&this._search||e.parent===this._currentRoot)&&i}).reduce((e,t)=>e.set(t.section,[...e.get(t.section)||[],t]),new Map);this._actionMatches=[...i.values()].flat(),0<this._actionMatches.length&&-1===this._selectedIndex&&(this._selected=this._actionMatches[0]),0===this._actionMatches.length&&(this._selected=void 0);let n=e=>r` ${He(e,e=>e.id,t=>{var e;return r`<ninja-action
            exportparts="ninja-action,ninja-selected,ninja-icon"
            .selected=${Te(t.id===(null==(e=this._selected)?void 0:e.id))}
            .hotKeysJoinedView=${this.hotKeysJoinedView}
            @mouseover=${e=>this._actionFocused(t,e)}
            @actionsSelected=${e=>this._actionSelected(e.detail)}
            .action=${t}
          ></ninja-action>`})}`,s=[];return i.forEach((e,t)=>{t=t?r`<div class="group-header">${t}</div>`:void 0;s.push(r`${t}${n(e)}`)}),r`
      <div @click=${this._overlayClick} class=${Je(t)}>
        <div class=${Je(e)} @animationend=${this._onTransitionEnd}>
          <ninja-header
            exportparts="ninja-input,ninja-input-wrapper"
            ${Fe(this._headerRef)}
            .placeholder=${this.placeholder}
            .hideBreadcrumbs=${this.hideBreadcrumbs}
            .breadcrumbs=${this.breadcrumbs}
            @change=${this._handleInput}
            @setParent=${e=>this.setParent(e.detail.parent)}
            @close=${this.close}
          >
          </ninja-header>
          <div class="modal-body">
            <div class="actions-list" part="actions-list">${s}</div>
          </div>
          <slot name="footer"> ${ri} </slot>
        </div>
      </div>
    `}get _selectedIndex(){return this._selected?this._actionMatches.indexOf(this._selected):-1}_actionSelected(t){var e;if(this.dispatchEvent(new CustomEvent("selected",{detail:{search:this._search,action:t},bubbles:!0,composed:!0})),t){if(t.children&&0<(null==(e=t.children)?void 0:e.length)&&(this._currentRoot=t.id,this._search=""),this._headerRef.value.setSearch(""),this._headerRef.value.focusSearch(),t.handler){let e=t.handler(t);null!=e&&e.keepOpen||this.close()}this._bump=!0}}async _handleInput(e){this._search=e.detail.search,await this.updateComplete,this.dispatchEvent(new CustomEvent("change",{detail:{search:this._search,actions:this._actionMatches},bubbles:!0,composed:!0}))}_overlayClick(e){null!=(e=e.target)&&e.classList.contains("modal")&&this.close()}};i.styles=[oi],H([o({type:String})],i.prototype,"placeholder",void 0),H([o({type:Boolean})],i.prototype,"disableHotkeys",void 0),H([o({type:Boolean})],i.prototype,"hideBreadcrumbs",void 0),H([o()],i.prototype,"openHotkey",void 0),H([o()],i.prototype,"navigationUpHotkey",void 0),H([o()],i.prototype,"navigationDownHotkey",void 0),H([o()],i.prototype,"closeHotkey",void 0),H([o()],i.prototype,"goBackHotkey",void 0),H([o()],i.prototype,"selectHotkey",void 0),H([o({type:Boolean})],i.prototype,"hotKeysJoinedView",void 0),H([o({type:Boolean})],i.prototype,"noAutoLoadMdIcons",void 0),H([o({type:Array,hasChanged:()=>!0})],i.prototype,"data",void 0),H([a()],i.prototype,"visible",void 0),H([a()],i.prototype,"_bump",void 0),H([a()],i.prototype,"_actionMatches",void 0),H([a()],i.prototype,"_search",void 0),H([a()],i.prototype,"_currentRoot",void 0),H([a()],i.prototype,"_flatData",void 0),H([a()],i.prototype,"breadcrumbs",null),H([a()],i.prototype,"_selected",void 0),H([Ae("ninja-keys")],i)}}]);