(window.webpackJsonpfeffery_utils_components=window.webpackJsonpfeffery_utils_components||[]).push([[25],{505:function(t,e,r){r.r(e);var j=r(1),P=r(662),n=r(204),z=r(25);function i(t){return(i="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t})(t)}function l(e,t){var r,n=Object.keys(e);return Object.getOwnPropertySymbols&&(r=Object.getOwnPropertySymbols(e),t&&(r=r.filter(function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable})),n.push.apply(n,r)),n}function A(n){for(var t=1;t<arguments.length;t++){var o=null!=arguments[t]?arguments[t]:{};t%2?l(Object(o),!0).forEach(function(t){var e,r;e=n,t=o[r=t],(r=function(){var t=function(t,e){if("object"!=i(t)||!t)return t;var r=t[Symbol.toPrimitive];if(void 0===r)return String(t);r=r.call(t,e);if("object"!=i(r))return r;throw new TypeError("@@toPrimitive must return a primitive value.")}(r,"string");return"symbol"==i(t)?t:t+""}())in e?Object.defineProperty(e,r,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[r]=t}):Object.getOwnPropertyDescriptors?Object.defineProperties(n,Object.getOwnPropertyDescriptors(o)):l(Object(o)).forEach(function(t){Object.defineProperty(n,t,Object.getOwnPropertyDescriptor(o,t))})}return n}function E(t,e){(null==e||e>t.length)&&(e=t.length);for(var r=0,n=Array(e);r<e;r++)n[r]=t[r];return n}function o(t){var e=t.id,r=t.key,n=t.children,o=t.className,i=t.style,l=t.size,u=t.defaultSize,a=t.minWidth,c=t.minHeight,s=t.maxWidth,f=t.maxHeight,y=t.direction,d=t.grid,b=t.bounds,p=t.boundsSelector,m=t.handleStyles,h=t.handleClassNames,g=t.setProps,v=t.loading_state;Object(j.useEffect)(function(){!l&&u&&g({size:u})},[]);var w,O=Object(z.clone)({top:!1,right:!1,bottom:!1,left:!1,topRight:!1,bottomRight:!1,bottomLeft:!1,topLeft:!1}),S=function(t,e){var r,n,o,i,l="undefined"!=typeof Symbol&&t[Symbol.iterator]||t["@@iterator"];if(l)return o=!(n=!0),{s:function(){l=l.call(t)},n:function(){var t=l.next();return n=t.done,t},e:function(t){o=!0,r=t},f:function(){try{n||null==l.return||l.return()}finally{if(o)throw r}}};if(Array.isArray(t)||(l=function(t,e){var r;if(t)return"string"==typeof t?E(t,e):"Map"===(r="Object"===(r={}.toString.call(t).slice(8,-1))&&t.constructor?t.constructor.name:r)||"Set"===r?Array.from(t):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?E(t,e):void 0}(t))||e&&t&&"number"==typeof t.length)return l&&(t=l),i=0,{s:e=function(){},n:function(){return i>=t.length?{done:!0}:{done:!1,value:t[i++]}},e:function(t){throw t},f:e};throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}(y);try{for(S.s();!(w=S.n()).done;)O[w.value]=!0}catch(t){S.e(t)}finally{S.f()}return React.createElement(P.a,{id:e,key:r,children:n,className:o,style:i,size:l,defaultSize:u,minWidth:a,minHeight:c,maxWidth:s,maxHeight:f,grid:d,bounds:p?document.querySelector(p):b,enable:O,handleStyles:A(A({},m),{},{top:A({cursor:"ns-resize"},null==m?void 0:m.top),right:A({cursor:"ew-resize"},null==m?void 0:m.right),bottom:A({cursor:"ns-resize"},null==m?void 0:m.bottom),left:A({cursor:"ew-resize"},null==m?void 0:m.left)}),handleClasses:h,onResizeStop:function(t,e,r,n){l&&g({size:{width:l.width+n.width,height:l.height+n.height}})},"data-dash-is-loading":v&&v.is_loading||void 0},n)}(e.default=o).defaultProps=n.b,o.propTypes=n.c}}]);