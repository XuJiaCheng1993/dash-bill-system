-- billwebsys.bill_dict_base definition

CREATE TABLE `bill_dict_base` (
  `dict_id` varchar(20) NOT NULL COMMENT '字典编号',
  `dict_cn_name` varchar(100) NOT NULL COMMENT '字典中文名称',
  `dict_en_name` varchar(50) NOT NULL COMMENT '字典英文名称',
  `icon` varchar(30) NOT NULL COMMENT '字典图标',
  `icon_color` varchar(10) NOT NULL COMMENT '图标颜色',
  `css_style` varchar(100) NOT NULL COMMENT 'CSS样式',
  `max_lv` int NOT NULL COMMENT '最大层级',
  PRIMARY KEY (`dict_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='基础账单字典表';


-- billwebsys.bill_dict_data definition

CREATE TABLE `bill_dict_data` (
  `dict_id` bigint NOT NULL COMMENT '字典编号',
  `dict_id_base` varchar(20) DEFAULT NULL COMMENT '基础字典编号',
  `dict_cn_name` varchar(100) NOT NULL COMMENT '字典中文名称',
  `dict_en_name` varchar(50) NOT NULL COMMENT '字典英文名称',
  `code_key` varchar(15) NOT NULL COMMENT '码键',
  `father_key` varchar(15) DEFAULT NULL COMMENT '父键',
  `level` int NOT NULL COMMENT '所处层级',
  `code_sort` int DEFAULT NULL COMMENT '码键顺序',
  `code_value` varchar(60) NOT NULL COMMENT '码值',
  `icon` varchar(50) DEFAULT NULL COMMENT '图标',
  `icon_color` varchar(10) DEFAULT NULL COMMENT '图标颜色',
  `icon_css` varchar(100) DEFAULT NULL COMMENT '其他CSS样式',
  `is_default` varchar(4) DEFAULT NULL COMMENT '是否默认',
  `status` varchar(4) NOT NULL COMMENT '码值状态',
  `create_by` varchar(60) NOT NULL COMMENT '创建者',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_by` varchar(60) NOT NULL COMMENT '更新者',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  `theme_id` bigint NOT NULL COMMENT '主题编号',
  PRIMARY KEY (`dict_id`,`code_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='账单字典码值表';


-- billwebsys.bill_dict_data_base definition

CREATE TABLE `bill_dict_data_base` (
  `dict_id` varchar(20) NOT NULL COMMENT '字典编号',
  `code_key` varchar(15) NOT NULL COMMENT '码键',
  `father_key` varchar(15) DEFAULT NULL COMMENT '父键',
  `level` int NOT NULL COMMENT '所处层级',
  `code_sort` int DEFAULT NULL COMMENT '码键顺序',
  `code_value` varchar(60) NOT NULL COMMENT '码值',
  `icon` varchar(50) DEFAULT NULL COMMENT '图标',
  `icon_color` varchar(10) DEFAULT NULL COMMENT '图标颜色',
  `icon_css` varchar(100) DEFAULT NULL COMMENT '其他CSS样式',
  `is_default` varchar(4) DEFAULT NULL COMMENT '是否默认',
  PRIMARY KEY (`dict_id`,`code_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='基础账单字典码值表';


-- billwebsys.bill_theme definition

CREATE TABLE `bill_theme` (
  `theme_id` bigint NOT NULL AUTO_INCREMENT COMMENT '主题编号',
  `theme_label` varchar(40) DEFAULT NULL COMMENT '主题名称',
  `theme_desc` varchar(100) DEFAULT NULL COMMENT '主题描述',
  `theme_status` varchar(4) NOT NULL COMMENT '主题状态',
  `create_by` varchar(60) NOT NULL COMMENT '创建者',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_by` varchar(60) NOT NULL COMMENT '更新者',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`theme_id`),
  UNIQUE KEY `theme_label` (`theme_label`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='账单主题信息表';


-- billwebsys.f_bill_data definition

CREATE TABLE `f_bill_data` (
  `bill_id` varchar(60) NOT NULL COMMENT '账单编号',
  `bill_type` varchar(15) NOT NULL COMMENT '账单类型编码',
  `bill_name` varchar(15) NOT NULL COMMENT '账单名称编码',
  `pay_channel` varchar(15) NOT NULL COMMENT '支付渠道编码',
  `settle_channel` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '结算渠道编码',
  `consume_object` varchar(15) NOT NULL COMMENT '消费对象编码',
  `bill_scene` varchar(15) NOT NULL COMMENT '账单场景编码',
  `bill_status` varchar(15) NOT NULL COMMENT '账单状态编码',
  `bill_amount` decimal(10,2) NOT NULL COMMENT '账单金额',
  `bill_date` date NOT NULL COMMENT '账单日期',
  `remark` varchar(600) DEFAULT NULL COMMENT '备注',
  `user_id` varchar(60) NOT NULL COMMENT '创建用户编号',
  `theme_id` bigint NOT NULL COMMENT '账单字典主题编号',
  `into_unix_time` bigint NOT NULL COMMENT '录入时间戳',
  PRIMARY KEY (`bill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='账单主题信息表';


-- billwebsys.sys_login_log definition

CREATE TABLE `sys_login_log` (
  `info_id` int NOT NULL AUTO_INCREMENT COMMENT '访问日志自增ID',
  `user_name` varchar(50) DEFAULT NULL COMMENT '用户账号',
  `ipaddr` varchar(128) DEFAULT NULL COMMENT '登录IP地址',
  `browser` varchar(50) DEFAULT NULL COMMENT '浏览器类型',
  `os` varchar(50) DEFAULT NULL COMMENT '操作系统',
  `status` varchar(1) DEFAULT NULL COMMENT '登录状态（S成功 F失败）',
  `msg` varchar(255) DEFAULT NULL COMMENT '提示消息',
  `login_time` datetime DEFAULT NULL COMMENT '访问时间',
  PRIMARY KEY (`info_id`),
  KEY `idx_sys_login_log_s` (`status`),
  KEY `idx_sys_login_log_lt` (`login_time`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='系统访问记录表';


-- billwebsys.sys_oper_log definition

CREATE TABLE `sys_oper_log` (
  `oper_id` bigint NOT NULL AUTO_INCREMENT COMMENT '日志主键',
  `title` varchar(50) DEFAULT NULL COMMENT '模块标题',
  `business_type` int DEFAULT NULL COMMENT '业务类型（0其它 1新增 2修改 3删除）',
  `method` varchar(100) DEFAULT NULL COMMENT '方法名称',
  `request_method` varchar(10) DEFAULT NULL COMMENT '请求方式',
  `operator_type` varchar(4) DEFAULT NULL COMMENT '操作类别（ot其它 pc后台用户 mob手机端用户）',
  `oper_user_id` varchar(50) DEFAULT NULL COMMENT '操作用户ID',
  `oper_name` varchar(50) DEFAULT NULL COMMENT '操作用户名称',
  `oper_url` varchar(255) DEFAULT NULL COMMENT '请求URL',
  `oper_ip` varchar(128) DEFAULT NULL COMMENT '主机地址',
  `oper_param` varchar(2000) DEFAULT NULL COMMENT '请求参数',
  `json_result` varchar(2000) DEFAULT NULL COMMENT '返回参数',
  `status` varchar(1) DEFAULT NULL COMMENT '操作状态（S成功 F失败）',
  `error_msg` varchar(2000) DEFAULT NULL COMMENT '错误消息',
  `oper_time` datetime DEFAULT NULL COMMENT '操作时间',
  `cost_time` bigint DEFAULT NULL COMMENT '消耗时间',
  PRIMARY KEY (`oper_id`),
  KEY `idx_sys_oper_log_s` (`status`),
  KEY `idx_sys_oper_log_ot` (`oper_time`),
  KEY `idx_sys_oper_log_bt` (`business_type`)
) ENGINE=InnoDB AUTO_INCREMENT=307 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='系统操作日志记录表';


-- billwebsys.sys_user definition

CREATE TABLE `sys_user` (
  `user_id` varchar(60) NOT NULL COMMENT '用户编号',
  `user_name` varchar(50) NOT NULL COMMENT '账户名称',
  `user_nick` varchar(50) NOT NULL COMMENT '账户昵称',
  `password` varchar(100) NOT NULL COMMENT '账户密码',
  `status` char(4) NOT NULL COMMENT '账户状态',
  `phone_number` varchar(11) DEFAULT NULL COMMENT '手机号',
  `email` varchar(30) DEFAULT NULL COMMENT '电子邮箱',
  `role` char(4) NOT NULL COMMENT '用户角色',
  `industry` varchar(30) DEFAULT NULL COMMENT '行业',
  `job` varchar(30) DEFAULT NULL COMMENT '职业',
  `theme_id` bigint NOT NULL COMMENT '当前使用的主题编号',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户信息表';


-- billwebsys.sys_user_bill_theme definition

CREATE TABLE `sys_user_bill_theme` (
  `user_id` varchar(60) NOT NULL COMMENT '用户编号',
  `theme_id` bigint NOT NULL COMMENT '主题编号',
  `status` char(4) NOT NULL COMMENT '关联状态',
  `operate_time` datetime NOT NULL COMMENT '关联时间',
  PRIMARY KEY (`user_id`,`theme_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户账单主题关联表';

INSERT INTO billwebsys.bill_dict_base (dict_id,dict_cn_name,dict_en_name,icon,icon_color,css_style,max_lv) VALUES
	 ('BD001','账单类型','billdict_bill_type','','','',2),
	 ('BD002','支付渠道','billdict_pay_channel','','','',2),
	 ('BD003','结算渠道','billdict_settle_channel','','','',2),
	 ('BD004','消费对象','billdict_consume_object','','','',1),
	 ('BD005','账单场景','billdict_bill_scene','','','',1),
	 ('BD006','账单状态','billdict_bill_status','','','',1);
INSERT INTO billwebsys.bill_dict_data (dict_id,dict_id_base,dict_cn_name,dict_en_name,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default,status,create_by,create_time,update_by,update_time,theme_id) VALUES
	 (1,'BD001','账单类型','billdict_bill_type','A','',1,1,'日用百货','','#20ff80','','1','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (2,'BD001','账单类型','billdict_bill_type','C','',1,3,'社交应酬','','#004cff','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (3,'BD001','账单类型','billdict_bill_type','E','',1,5,'住房物业','','#cd5c5c','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (4,'BD001','账单类型','billdict_bill_type','F','',1,6,'交通出行','','#008b8b','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (5,'BD001','账单类型','billdict_bill_type','G','',1,7,'汽车消费','','#9400d3','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (6,'BD001','账单类型','billdict_bill_type','H','',1,8,'服务消费','','#ffb6c1','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (7,'BD001','账单类型','billdict_bill_type','I','',1,9,'餐饮美食','','#ff8c00','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (8,'BD001','账单类型','billdict_bill_type','Z','',1,10,'其他','','#bb45cd','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (9,'BD001','账单类型','billdict_bill_type','A01','A',2,1,'服装','','#20ff80','','1','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (10,'BD001','账单类型','billdict_bill_type','A02','A',2,2,'百货','','#20ff8e','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1);
INSERT INTO billwebsys.bill_dict_data (dict_id,dict_id_base,dict_cn_name,dict_en_name,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default,status,create_by,create_time,update_by,update_time,theme_id) VALUES
	 (11,'BD001','账单类型','billdict_bill_type','A03','A',2,3,'家居','','#19cc71','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (12,'BD001','账单类型','billdict_bill_type','A04','A',2,4,'电器','','#129954','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (13,'BD001','账单类型','billdict_bill_type','C01','C',2,1,'份子','','#004cff','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (14,'BD001','账单类型','billdict_bill_type','C02','C',2,2,'探望','','#003ccc','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (15,'BD001','账单类型','billdict_bill_type','C03','C',2,3,'应酬','','#002d99','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (16,'BD001','账单类型','billdict_bill_type','C04','C',2,4,'红包','','#0191ff','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (17,'BD001','账单类型','billdict_bill_type','C05','C',2,5,'礼物','','#0080ff','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (18,'BD001','账单类型','billdict_bill_type','E01','E',2,1,'物业费','','#cd5c5c','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (19,'BD001','账单类型','billdict_bill_type','E02','E',2,2,'房贷','','#f36d6d','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (20,'BD001','账单类型','billdict_bill_type','E03','E',2,3,'房租','','#f36d6d','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1);
INSERT INTO billwebsys.bill_dict_data (dict_id,dict_id_base,dict_cn_name,dict_en_name,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default,status,create_by,create_time,update_by,update_time,theme_id) VALUES
	 (21,'BD001','账单类型','billdict_bill_type','F01','F',2,1,'公交地铁','','#008b8b','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (22,'BD001','账单类型','billdict_bill_type','F02','F',2,2,'共享单车','','#00b1b1','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (23,'BD001','账单类型','billdict_bill_type','F03','F',2,3,'打车费','','#007d7d','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (24,'BD001','账单类型','billdict_bill_type','F04','F',2,4,'高速费','','#004949','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (25,'BD001','账单类型','billdict_bill_type','F05','F',2,4,'动车高铁','','#003939','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (26,'BD001','账单类型','billdict_bill_type','G01','G',2,1,'保养费','','#9400d3','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (27,'BD001','账单类型','billdict_bill_type','G02','G',2,2,'油费','','#d400ff','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (28,'BD001','账单类型','billdict_bill_type','G03','G',2,3,'停车费','','#b200ff','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (29,'BD001','账单类型','billdict_bill_type','G04','G',2,4,'汽车用品','','#8e00cc','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (30,'BD001','账单类型','billdict_bill_type','G05','G',2,5,'汽车修理','','#6a0099','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1);
INSERT INTO billwebsys.bill_dict_data (dict_id,dict_id_base,dict_cn_name,dict_en_name,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default,status,create_by,create_time,update_by,update_time,theme_id) VALUES
	 (31,'BD001','账单类型','billdict_bill_type','G06','G',2,6,'汽车保险','','#35004c','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (32,'BD001','账单类型','billdict_bill_type','H01','H',2,1,'理发','','#ffb6c1','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (33,'BD001','账单类型','billdict_bill_type','H02','H',2,2,'课程','','#ffb6b7','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (34,'BD001','账单类型','billdict_bill_type','H03','H',2,4,'快递','','#996c6d','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (35,'BD001','账单类型','billdict_bill_type','H04','H',2,5,'礼庆','','#bf8788','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (36,'BD001','账单类型','billdict_bill_type','H05','H',2,6,'洗衣','','#bf7877','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (37,'BD001','账单类型','billdict_bill_type','I01','I',2,1,'正餐','','#ff8c00','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (38,'BD001','账单类型','billdict_bill_type','I02','I',2,2,'美食','','#998700','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (39,'BD001','账单类型','billdict_bill_type','I03','I',2,3,'奶茶饮料','','#cc7000','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (40,'BD001','账单类型','billdict_bill_type','I04','I',2,4,'水果','','#ff9d00','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1);
INSERT INTO billwebsys.bill_dict_data (dict_id,dict_id_base,dict_cn_name,dict_en_name,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default,status,create_by,create_time,update_by,update_time,theme_id) VALUES
	 (41,'BD001','账单类型','billdict_bill_type','Z01','Z',2,1,'其他','','#bb45cd','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (42,'BD002','支付渠道','billdict_pay_channel','B','',1,2,'银行支付','','#ff662f','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (43,'BD002','支付渠道','billdict_pay_channel','C','',1,3,'现金支付','','#bd4455','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (44,'BD002','支付渠道','billdict_pay_channel','H','',1,1,'互联网支付','','#4dc6bd','','1','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (45,'BD002','支付渠道','billdict_pay_channel','B001','B',2,4,'掌上生活APP','','#fa4947','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (46,'BD002','支付渠道','billdict_pay_channel','B002','B',2,1,'建设银行APP','','#003b90','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (47,'BD002','支付渠道','billdict_pay_channel','B003','B',2,2,'建行生活APP','','#fe9b42','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (48,'BD002','支付渠道','billdict_pay_channel','B004','B',2,7,'中国银行APP','','#b81c22','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (49,'BD002','支付渠道','billdict_pay_channel','B005','B',2,6,'买单吧APP','','#037dfe','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (50,'BD002','支付渠道','billdict_pay_channel','B006','B',2,5,'交通银行APP','','#1d2088','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1);
INSERT INTO billwebsys.bill_dict_data (dict_id,dict_id_base,dict_cn_name,dict_en_name,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default,status,create_by,create_time,update_by,update_time,theme_id) VALUES
	 (51,'BD002','支付渠道','billdict_pay_channel','B007','B',2,8,'农业银行APP','','#5cb0a3','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (52,'BD002','支付渠道','billdict_pay_channel','B008','B',2,3,'招商银行APP','','#e41e26','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (53,'BD002','支付渠道','billdict_pay_channel','B999','B',2,999,'其他银行APP','','#ff662f','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (54,'BD002','支付渠道','billdict_pay_channel','C001','C',2,1,'现金','','#bd4455','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (55,'BD002','支付渠道','billdict_pay_channel','C002','C',2,2,'数字人民币','','#e6001e','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (56,'BD002','支付渠道','billdict_pay_channel','H001','H',2,1,'支付宝支付','','#1777ff','','1','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (57,'BD002','支付渠道','billdict_pay_channel','H002','H',2,2,'微信支付','','#00d40b','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (58,'BD002','支付渠道','billdict_pay_channel','H003','H',2,3,'抖音支付','','#0a0b14','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (59,'BD002','支付渠道','billdict_pay_channel','H004','H',2,4,'美团支付','','#ffd100','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (60,'BD002','支付渠道','billdict_pay_channel','H005','H',2,5,'京东支付','','#ff3018','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1);
INSERT INTO billwebsys.bill_dict_data (dict_id,dict_id_base,dict_cn_name,dict_en_name,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default,status,create_by,create_time,update_by,update_time,theme_id) VALUES
	 (61,'BD002','支付渠道','billdict_pay_channel','H999','H',2,999,'其他互联网支付','','#4dc6bd','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (62,'BD003','结算渠道','billdict_settle_channel','HQ','',1,1,'互联网钱包','','#4dc6bd','','1','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (63,'BD003','结算渠道','billdict_settle_channel','XQ','',1,3,'现金钱包','','#bd4455','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (64,'BD003','结算渠道','billdict_settle_channel','YQ','',1,2,'银行钱包','','#ff662f','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (65,'BD003','结算渠道','billdict_settle_channel','HQ001','HQ',2,1,'支付宝钱包','','#1777ff','','1','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (66,'BD003','结算渠道','billdict_settle_channel','HQ002','HQ',2,2,'微信钱包','','#00d40b','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (67,'BD003','结算渠道','billdict_settle_channel','HQ003','HQ',2,3,'京东钱包','','#ff3018','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (68,'BD003','结算渠道','billdict_settle_channel','HQ004','HQ',2,4,'抖音钱包','','#0a0b14','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (69,'BD003','结算渠道','billdict_settle_channel','HQ999','HQ',2,999,'其他互联网钱包','','#4dc6bd','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (70,'BD003','结算渠道','billdict_settle_channel','XQ001','XQ',2,1,'现金钱包','','#bd4455','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1);
INSERT INTO billwebsys.bill_dict_data (dict_id,dict_id_base,dict_cn_name,dict_en_name,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default,status,create_by,create_time,update_by,update_time,theme_id) VALUES
	 (71,'BD003','结算渠道','billdict_settle_channel','YQ001','YQ',2,1,'中国银行','','#b81c22','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (72,'BD003','结算渠道','billdict_settle_channel','YQ002','YQ',2,2,'农业银行','','#5cb0a3','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (73,'BD003','结算渠道','billdict_settle_channel','YQ003','YQ',2,3,'工商银行','','#c6000b','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (74,'BD003','结算渠道','billdict_settle_channel','YQ004','YQ',2,4,'建设银行','','#003b90','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (75,'BD003','结算渠道','billdict_settle_channel','YQ005','YQ',2,5,'交通银行','','#1d2088','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (76,'BD003','结算渠道','billdict_settle_channel','YQ006','YQ',2,6,'招商银行','','#e41e26','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (77,'BD003','结算渠道','billdict_settle_channel','YQ999','YQ',2,999,'其他银行','','#ff662f','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (78,'BD004','消费对象','billdict_consume_object','FR','',1,2,'朋友','','','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (79,'BD004','消费对象','billdict_consume_object','HO','',1,3,'家人','','','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (80,'BD004','消费对象','billdict_consume_object','OT','',1,9,'其他','','','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1);
INSERT INTO billwebsys.bill_dict_data (dict_id,dict_id_base,dict_cn_name,dict_en_name,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default,status,create_by,create_time,update_by,update_time,theme_id) VALUES
	 (81,'BD004','消费对象','billdict_consume_object','SE','',1,1,'自己','','','','1','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (82,'BD005','账单场景','billdict_bill_scene','W','',1,1,'工作','','','','1','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (83,'BD005','账单场景','billdict_bill_scene','S','',1,2,'学习','','','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (84,'BD005','账单场景','billdict_bill_scene','Y','',1,3,'休闲','','','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (85,'BD006','账单状态','billdict_bill_status','00','',1,1,'正常','billstatus-zhengchang','#2ECC71','','1','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1),
	 (86,'BD006','账单状态','billdict_bill_status','01','',1,2,'退款','billstatus-tuikuan','#E74C3C','','0','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-01-01 00:00:00',1);
INSERT INTO billwebsys.bill_dict_data_base (dict_id,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default) VALUES
	 ('BD001','A','',1,1,'日用百货','','#20ff80','','1'),
	 ('BD001','A01','A',2,1,'服装','','#20ff80','','1'),
	 ('BD001','A02','A',2,2,'百货','','#20ff8e','','0'),
	 ('BD001','A03','A',2,3,'家居','','#19cc71','','0'),
	 ('BD001','A04','A',2,4,'电器','','#129954','','0'),
	 ('BD001','C','',1,3,'社交应酬','','#004cff','','0'),
	 ('BD001','C01','C',2,1,'份子','','#004cff','','0'),
	 ('BD001','C02','C',2,2,'探望','','#003ccc','','0'),
	 ('BD001','C03','C',2,3,'应酬','','#002d99','','0'),
	 ('BD001','C04','C',2,4,'红包','','#0191ff','','0');
INSERT INTO billwebsys.bill_dict_data_base (dict_id,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default) VALUES
	 ('BD001','C05','C',2,5,'礼物','','#0080ff','','0'),
	 ('BD001','E','',1,5,'住房物业','','#cd5c5c','','0'),
	 ('BD001','E01','E',2,1,'物业费','','#cd5c5c','','0'),
	 ('BD001','E02','E',2,2,'房贷','','#f36d6d','','0'),
	 ('BD001','E03','E',2,3,'房租','','#f36d6d','','0'),
	 ('BD001','F','',1,6,'交通出行','','#008b8b','','0'),
	 ('BD001','F01','F',2,1,'公交地铁','','#008b8b','','0'),
	 ('BD001','F02','F',2,2,'共享单车','','#00b1b1','','0'),
	 ('BD001','F03','F',2,3,'打车费','','#007d7d','','0'),
	 ('BD001','F04','F',2,4,'高速费','','#004949','','0');
INSERT INTO billwebsys.bill_dict_data_base (dict_id,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default) VALUES
	 ('BD001','F05','F',2,4,'动车高铁','','#003939','','0'),
	 ('BD001','G','',1,7,'汽车消费','','#9400d3','','0'),
	 ('BD001','G01','G',2,1,'保养费','','#9400d3','','0'),
	 ('BD001','G02','G',2,2,'油费','','#d400ff','','0'),
	 ('BD001','G03','G',2,3,'停车费','','#b200ff','','0'),
	 ('BD001','G04','G',2,4,'汽车用品','','#8e00cc','','0'),
	 ('BD001','G05','G',2,5,'汽车修理','','#6a0099','','0'),
	 ('BD001','G06','G',2,6,'汽车保险','','#35004c','','0'),
	 ('BD001','H','',1,8,'服务消费','','#ffb6c1','','0'),
	 ('BD001','H01','H',2,1,'理发','','#ffb6c1','','0');
INSERT INTO billwebsys.bill_dict_data_base (dict_id,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default) VALUES
	 ('BD001','H02','H',2,2,'课程','','#ffb6b7','','0'),
	 ('BD001','H03','H',2,4,'快递','','#996c6d','','0'),
	 ('BD001','H04','H',2,5,'礼庆','','#bf8788','','0'),
	 ('BD001','H05','H',2,6,'洗衣','','#bf7877','','0'),
	 ('BD001','I','',1,9,'餐饮美食','','#ff8c00','','0'),
	 ('BD001','I01','I',2,1,'正餐','','#ff8c00','','0'),
	 ('BD001','I02','I',2,2,'美食','','#998700','','0'),
	 ('BD001','I03','I',2,3,'奶茶饮料','','#cc7000','','0'),
	 ('BD001','I04','I',2,4,'水果','','#ff9d00','','0'),
	 ('BD001','Z','',1,10,'其他','','#bb45cd','','0');
INSERT INTO billwebsys.bill_dict_data_base (dict_id,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default) VALUES
	 ('BD001','Z01','Z',2,1,'其他','','#bb45cd','','0'),
	 ('BD002','B','',1,2,'银行支付','','#ff662f','','0'),
	 ('BD002','B001','B',2,4,'掌上生活APP','','#fa4947','','0'),
	 ('BD002','B002','B',2,1,'建设银行APP','','#003b90','','0'),
	 ('BD002','B003','B',2,2,'建行生活APP','','#fe9b42','','0'),
	 ('BD002','B004','B',2,7,'中国银行APP','','#b81c22','','0'),
	 ('BD002','B005','B',2,6,'买单吧APP','','#037dfe','','0'),
	 ('BD002','B006','B',2,5,'交通银行APP','','#1d2088','','0'),
	 ('BD002','B007','B',2,8,'农业银行APP','','#5cb0a3','','0'),
	 ('BD002','B008','B',2,3,'招商银行APP','','#e41e26','','0');
INSERT INTO billwebsys.bill_dict_data_base (dict_id,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default) VALUES
	 ('BD002','B999','B',2,999,'其他银行APP','','#ff662f','','0'),
	 ('BD002','C','',1,3,'现金支付','','#bd4455','','0'),
	 ('BD002','C001','C',2,1,'现金','','#bd4455','','0'),
	 ('BD002','C002','C',2,2,'数字人民币','','#e6001e','','0'),
	 ('BD002','H','',1,1,'互联网支付','','#4dc6bd','','1'),
	 ('BD002','H001','H',2,1,'支付宝支付','','#1777ff','','1'),
	 ('BD002','H002','H',2,2,'微信支付','','#00d40b','','0'),
	 ('BD002','H003','H',2,3,'抖音支付','','#0a0b14','','0'),
	 ('BD002','H004','H',2,4,'美团支付','','#ffd100','','0'),
	 ('BD002','H005','H',2,5,'京东支付','','#ff3018','','0');
INSERT INTO billwebsys.bill_dict_data_base (dict_id,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default) VALUES
	 ('BD002','H999','H',2,999,'其他互联网支付','','#4dc6bd','','0'),
	 ('BD003','HQ','',1,1,'互联网钱包','','#4dc6bd','','1'),
	 ('BD003','HQ001','HQ',2,1,'支付宝钱包','','#1777ff','','1'),
	 ('BD003','HQ002','HQ',2,2,'微信钱包','','#00d40b','','0'),
	 ('BD003','HQ003','HQ',2,3,'京东钱包','','#ff3018','','0'),
	 ('BD003','HQ004','HQ',2,4,'抖音钱包','','#0a0b14','','0'),
	 ('BD003','HQ999','HQ',2,999,'其他互联网钱包','','#4dc6bd','','0'),
	 ('BD003','XQ','',1,3,'现金钱包','','#bd4455','','0'),
	 ('BD003','XQ001','XQ',2,1,'现金钱包','','#bd4455','','0'),
	 ('BD003','YQ','',1,2,'银行钱包','','#ff662f','','0');
INSERT INTO billwebsys.bill_dict_data_base (dict_id,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default) VALUES
	 ('BD003','YQ001','YQ',2,1,'中国银行','','#b81c22','','0'),
	 ('BD003','YQ002','YQ',2,2,'农业银行','','#5cb0a3','','0'),
	 ('BD003','YQ003','YQ',2,3,'工商银行','','#c6000b','','0'),
	 ('BD003','YQ004','YQ',2,4,'建设银行','','#003b90','','0'),
	 ('BD003','YQ005','YQ',2,5,'交通银行','','#1d2088','','0'),
	 ('BD003','YQ006','YQ',2,6,'招商银行','','#e41e26','','0'),
	 ('BD003','YQ999','YQ',2,999,'其他银行','','#ff662f','','0'),
	 ('BD004','FR','',1,2,'朋友','','','','0'),
	 ('BD004','HO','',1,3,'家人','','','','0'),
	 ('BD004','OT','',1,9,'其他','','','','0');
INSERT INTO billwebsys.bill_dict_data_base (dict_id,code_key,father_key,`level`,code_sort,code_value,icon,icon_color,icon_css,is_default) VALUES
	 ('BD004','SE','',1,1,'自己','','','','1'),
	 ('BD005','S','',1,2,'学习','','','','0'),
	 ('BD005','W','',1,1,'工作','','','','1'),
	 ('BD005','Y','',1,3,'休闲','','','','0'),
	 ('BD006','00','',1,1,'正常','billstatus-zhengchang','#2ECC71','','1'),
	 ('BD006','01','',1,2,'退款','billstatus-tuikuan','#E74C3C','','0');
INSERT INTO billwebsys.bill_theme (theme_label,theme_desc,theme_status,create_by,create_time,update_by,update_time) VALUES
	 ('默认主题','系统自带的主题','1','SYS0001','2024-01-01 00:00:00','SYS0001','2024-11-15 21:30:27');
INSERT INTO billwebsys.sys_user (user_id,user_name,user_nick,password,status,phone_number,email,`role`,industry,job,theme_id,create_time,update_time) VALUES
	 ('SYS0001','admin','管理者的账号','$2b$12$ydthNWMCxLhuFRQNmywRH.tfND/w6SnU5purhL68VqZVOgoNnWUNu','1','12345678910','xxyyot@88vip.com','A1','制造业','UI设计师',1,'2024-01-01 00:00:00','2024-12-02 21:31:59');
INSERT INTO billwebsys.sys_user_bill_theme (user_id,theme_id,status,operate_time) VALUES
	 ('SYS0001',1,'1','2024-01-01 00:00:00');
