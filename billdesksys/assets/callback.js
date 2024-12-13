window.dash_clientside = Object.assign({}, window.dash_clientside, {
    billAdd: {
        // 弹出添加账单的MODAL
        showModalAddBill: ( nClicks ) => {
            if (nClicks) {
                window.dash_clientside.set_props(
                    "billAdd-modal-addBillData",
                    {
                        "visible": true
                    }
                )
                
                window.dash_clientside.set_props(
                    "billAdd-modal-addBillData",
                    {
                        "key": Math.random().toString().substring(2, 8)
                    }
                )


            }
        },


        // 切换账单状态的图标
        switchBillStatusIcon: ( nClicks, checked, options ) => {
            if ( nClicks && options)  {
                checked = !checked

                if ( checked ){
                    window.dash_clientside.set_props(
                        "billAdd-I-billStatusIcon",
                        {
                            "class": options.bill_status.check.icon,
                            "style" : {'color': options.bill_status.check.color, 'font-size': '24px'}
                        }
                    ) 
                }
                else {
                    window.dash_clientside.set_props(
                        "billAdd-I-billStatusIcon",
                        {
                            "class": options.bill_status.uncheck.icon,
                            "style" : {'color': options.bill_status.uncheck.color, 'font-size': '24px'}
                        }
                    )         
                }
        
            }
            return checked;
        },


        // // 重置添加账单对话框的数据
        resetAddBillData: (nClicks) => {
            if ( nClicks ) {
                let values = {
                    'billadd-calendar-bill-date': undefined,
                    'billadd-treeselect-bill-name': undefined, 
                    'billadd-inputnumber-bill-amount': undefined, 
                    'billadd-treeselect-pay-channel': undefined, 
                    'billadd-treeselect-settle-channel': undefined, 
                    'billadd-radiogroup-bill-object': undefined, 
                    'billadd-radiogroup-bill-scene': undefined,
                    'billadd-input-remark': undefined
                    }
                return [values, true];
            } else {
                return [window.dash_clientside.no_update, window.dash_clientside.no_update];
            } 
        },
    
        // 初始化添加账单对话框的数据
        initAddBillData:(visible) => {
            if ( visible ) {
                return [window.dash_clientside.no_update, window.dash_clientside.no_update];
            } else {
                let values = {
                    'billadd-calendar-bill-date': undefined,
                    'billadd-treeselect-bill-name': undefined, 
                    'billadd-inputnumber-bill-amount': undefined, 
                    'billadd-treeselect-pay-channel': undefined, 
                    'billadd-treeselect-settle-channel': undefined, 
                    'billadd-radiogroup-bill-object': undefined, 
                    'billadd-radiogroup-bill-scene': undefined,
                    'billadd-input-remark': undefined
                    }
                return [values, true];
            }
            
        },

        // 检验日期选择输入
        checkBillDateStatus: ( val ) => {
            if (val === undefined || val === '') {
                return 'error';
            } else {
                return undefined;
            }
        },


        // 检验账单类型的选择框是否符合规范
        checkBillNameStatus: ( val ) => {
            if (val === undefined || val === '') {
                return ['error', "账单类型不能为空"];
            } else {
                return ['success', undefined];
            }
        },


        // 检验账单金额的填写框是否符合规范
        checkBillAmountStatus: ( val ) => {
            // 不能为空判断
            if (val === undefined || val === '') {
                return ['error', "请选择账单类型"];
            }   
            
            const amountPattern = /^[-+]?\d*(\.\d+)?$/;
            if ( !amountPattern.test( val ) ){
                return ['error', "账单金额只能为数字"];
            }

            return ['success', undefined];
            
        },

        // 检验账单场景的选择框是否符合规范
        checkBillSceneStatus: ( val ) => {
            if (val === undefined || val === '') {
                return ['error', "账单类型不能为空"];
            } else {
                return ['success', undefined];
            }
        },

    },

    PlatformManage:{
        // 弹出修改用户信息和重置密码的modal
        showReviseResetUserInfoModal:(clickedKey, nClicks) => {
            let out = [false, false]
            
            if (nClicks === undefined) {
                return out;
            } else {
                if (clickedKey === 'revise-account'){
                    out[0] = true;
                } 
                 
                if (clickedKey === 'revise-password'){
                    out[1] = true;
                } 
                     
                return out;
                
            }
        },


        // 检验密码是否符合规范-最小长度6位
        checkPasswordRule: (password) => {
            if (password){
                if (password.length >= 6){
                    return ['success', undefined];
                } else {
                    return ['error', "密码长度不能小于6位"];
                }
            }
            return [window.dash_clientside.no_update, window.dash_clientside.no_update];
         },
         
        
        // 检验两次输入的密码是否一致
        checkPassword1and2: (password_confirm, password) => {
            if (password_confirm && password){
                if (password_confirm === password){
                    return ['success', undefined];
                } else {
                    return ['error', "两次输入的密码不一致",];
                }
            }
            return [window.dash_clientside.no_update, window.dash_clientside.no_update];
        },

        
        // 检验是否是中国大陆手机号
        checkPhoneNumberRule: (phone) => {
            if (phone === undefined || phone === ''){
                return [undefined, "请输入修改后的手机号"];
            }
            else{
                const phoneRegex = /^1[3-9]\d{9}$/;
                if (!phoneRegex.test(phone)){
                    return ['error', "请输入正确的中国大陆手机号"];
                } else {
                    return ['success', "请输入修改后的手机号"];
                };
            }
        },
        
        // 检验是否满足电子邮件地址规则
        checkEmailRule: (email) => {
            if (email === undefined || email === ''){
                return [undefined, "请输入修改后的电子邮箱"];
            }
            else {
                const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
                if (!emailRegex.test(email)){
                    return ['error', "请输入正确的电子邮箱地址"];
                } else {
                    return ['success', "请输入修改后的电子邮箱"];
                };
            }

        },

        
    },


    Login: {
        // 检验验证码是否填写正确
        checkCaptcha: (captcha_input, captcha) => {
            if ( captcha_input){
                if ( captcha_input === captcha){
                    return ['success', undefined, true];
                }
            }
            return ['error', '验证码输入错误！', false];
        },

        


    },

    BillManage: {
        // 切换账单状态的Switch组件
        switchBillStatusCheck:(nClicks, checked) => {
            if (nClicks){
                checked = !checked
            }
            return checked;
        },


        // 切换账单状态的图标
        switchBillStatusIcon: (checked, options ) => {
            if (options)  {
                if ( checked ){
                    window.dash_clientside.set_props(
                        "billManage-I-billStatusIcon",
                        {
                            "class": options.bill_status.check.icon,
                            "style" : {'color': options.bill_status.check.color, 'font-size': '24px'}
                        }
                    ) 
                }
                else {
                    window.dash_clientside.set_props(
                        "billManage-I-billStatusIcon",
                        {
                            "class": options.bill_status.uncheck.icon,
                            "style" : {'color': options.bill_status.uncheck.color, 'font-size': '24px'}
                        }
                    )         
                }
                return undefined;
            }

        },

        // 重置账单查询条件
        resetQueryBillConditions: (nClicks) => {
            if ( nClicks ) {
                let values = {
                    'billManage-dateRangePicker-billDate': undefined,
                    'billManage-select-billType': undefined, 
                    'billManage-select-billStatus': undefined, 
                    'billManage-treeSelect-payChannel': undefined, 
                    'billManage-treeSelect-settleChannel': undefined
                    }
                return values;
            } else {
                return window.dash_clientside.no_update;
            } 
        },

        // // 账单修改的MODAL中根据账单名称自适应更改账单类型
        // syncBillTypeAccordBillNameInReviseBillModal: (bill_name_key) => {
        //     if (bill_name_key){
        //         return bill_name_key[0];
        //     } else {
        //         return undefined;
        //     }
        // },




    },


    BillConfig:{
        // 码值项中的图标选择渲染
        rederCodeItemIcon: (icon_add, icon_edit) => {
            let { inputs_list, triggered_id, triggered } = window.dash_clientside.callback_context;
            if (triggered_id === 'config-radioGroup-iconList-editCode'){
                let icon_edit_elm = {
                'props': {
                    'icon': icon_edit
                },
                'type': 'AntdIcon',
                'namespace': 'feffery_antd_components'
                }
                return [null, null, icon_edit, icon_edit_elm];               
            }
            
            if (triggered_id === 'config-radioGroup-iconList-addCode'){
                let icon_add_elm = {
                'props': {
                    'icon': icon_add
                },
                'type': 'AntdIcon',
                'namespace': 'feffery_antd_components'
                }
                return [icon_add, icon_add_elm, null, null];
            }
            
            return [null, null, null, null];
        },

        // 重置新增字典项的表单
        resetAddCodeFormItem: (nClicks) => {
            if ( nClicks ) {
                let outputs =  [undefined, undefined, undefined, undefined, undefined, undefined, undefined, undefined]
                return outputs
            } else {
                return window.dash_clientside.no_update;
            } 
        },

        // 关闭编辑编辑码值项的MODAL
        cancelEditCodeItem: (nClicks) => {
            if ( nClicks ) {
                return false
            } 
            return false;
        },

        // 展开新增主题/编辑主题的Modal
        renderAddOrEditBillThemeModal : ( nClicks ) => {
            let { inputs_list, triggered_id, triggered } = window.dash_clientside.callback_context;
            if ( nClicks ){
                
                if (triggered_id.index === "add"){
                    window.dash_clientside.set_props(
                        "config-modal-addTheme",
                        {
                            "visible": true
                        }
                    )
                }
                
                if (triggered_id.index === "edit"){
                    window.dash_clientside.set_props(
                        "config-modal-editTheme",
                        {
                            "visible": true
                        }
                    )
                }
                             
            }
        },

        // 渲染新增账单字典的 modal
        renderCodeItemAddModal:(nClicks, content, billId, oldCodes) => {
            if (nClicks) {
                const themeId = sessionStorage.getItem('theme_id');
                const dictInfo = billId.split('-');
                let dictIdBase, codeKey, level;
        
                if (dictInfo.length <= 1) {
                    dictIdBase = dictInfo[0];
                    codeKey = '';
                    level = 1;
                } else {
                    [dictIdBase, codeKey] = dictInfo;
                    level = 2;
                }
        
                let dictCnName = '', dictEnName = '';
        
                for (let ii of oldCodes) {
                    if (ii.dict_id_base === dictIdBase) {
                        dictCnName = ii.dict_cn_name;
                        dictEnName = ii.dict_en_name;
                        break;
                    }
                }
        
                if (content === '新增') {
                    return [true, `No.${themeId}`, dictCnName, dictIdBase, dictEnName, codeKey, String(level)];
                }
            }
        
            return [false, undefined, undefined, undefined, undefined, undefined, undefined];
        }


        
    },

    
    BillAnalyze:{
        // 判断账单日历是否需要更新数据
        checkIsNeedUpdateBillCalendar : (choiceDate, event, lastEventInfo) => {   
            // 如果event未定义或为空，则直接返回需要更新
            if (event === undefined || event === null){
                return [undefined, true];
            }

            // 当前的事件信息
            let curEventInfo = { choiceDate: choiceDate, event: event.type };
        
            // 如果上次事件信息为空
            if (lastEventInfo === null || lastEventInfo === undefined) {
                return [curEventInfo, true];
            }
        
            // 获取上次事件信息
            let lstEvent = lastEventInfo.event;
            let lstChoiceDate = lastEventInfo.choiceDate;
        
            // 如果两次事件相同
            if (lstEvent === event.type) {
                // 年份不同需要更新
                if (event.type === 'month') {
                    return [
                        curEventInfo,
                        choiceDate.substring(0, 4) !== lstChoiceDate.substring(0, 4)
                    ];
                }
        
                // 月份不同需要更新
                else {
                    return [
                        curEventInfo,
                        choiceDate.substring(0, 7) !== lstChoiceDate.substring(0, 7)
                    ];
                }
            }
        
            // 如果两次事件不相同
            if (lstEvent === 'date' && event.type === 'month') {
                return [
                    curEventInfo,
                    choiceDate.substring(0, 4) !== lstChoiceDate.substring(0, 4)
                ];
            }
        
            // 如果两次事件不相同
            if (lstEvent === 'month' && event.type === 'date') {
                return [
                    curEventInfo,
                    true
                ];
            }
        
            return [curEventInfo, false];
        },

        // 渲染账单分析维度选择卡
        checkAndUpdateAnalyzeDimCard: (choices, choiceList) => {
            const hit = '※';
            const oriName = {
                bill_date: '账单日期',
                bill_type: '账单类型',
                consume_object: '消费对象',
                pay_channel: '支付渠道',
                settle_channel: '结算渠道',
                bill_scene: '支出场景'
            };
            const choiceName = choiceList.map(c => oriName[c]);
            const disabled = Array(choiceList.length).fill(false);
                     
            if (choices) {
                
                choices.forEach((c, i) => {
                    choiceName[choiceList.indexOf(c)] = `${hit}${i + 1} ${oriName[c]}`;
                });
                
                if (choices.length >= 2) {
                    const disabled = Array(choiceList.length).fill(true);
                    choices.forEach(c => {
                        disabled[choiceList.indexOf(c)] = false;
                    });
                    return [disabled, choiceName];
                } 
                
                return [disabled, choiceName];               
            }
        
            return [disabled, choiceName];
        }
        

        
        
    },

    
});


