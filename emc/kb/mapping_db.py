#-*- coding: UTF-8 -*-
import sqlalchemy.types
import sqlalchemy.schema
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Sequence
from five import grok
from zope import schema
from zope.interface import Interface,implements
from emc.kb import ORMBase
from emc.kb import _

########################################
# """
# 约定:
# 1. 所有table名称,以汉语拼音命名,但只有前两个汉字用全拼音,其他只取声母,所有字母小写;
# 2. 表名加数据库名前缀,数据库名取英文前四位,para_fashej
# 3. 所有表对应的python mapper 类的名称规则是:字母组成同表名,但首字母大写;
# 4. 所有表对应的python mapper的接口类名称规则:python mapper 类名称前加大写I
# 5. 所有表主键名称为id,为整型,自增长
# """
#############################################
class IModel(Interface):
    """编号number 记录表
    """
    id = schema.Int(
            title=_(u"model table primary key"),
        )   
    # 型号代码
    xhdm = schema.TextLine(
            title=_(u"model code"),
        )    
    #型号名称
    xhmc = schema.TextLine(
            title=_(u"model name"),
        )

class Model(ORMBase):
    """Database-backed implementation of IModel
    """
    implements(IModel)
    
    __tablename__ = 'model'
    
    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('model_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
        
    xhdm = sqlalchemy.schema.Column(sqlalchemy.types.String(8),
            nullable=False,
        )
    xhmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    
    
class IFashej(Interface):
    """发射机
    """
    id = schema.Int(
            title=_(u"table primary key"),
        )
    sbdm = schema.TextLine(
            title=_(u"she bei dai ma"),
        )
    sbmc = schema.TextLine(
            title=_(u"fa she ji ming cheng"),
        )
    # 分系统代码
    pcdm = schema.TextLine(
            title=_(u"zhuang tai pi ci dai ma"),
        )
    #分系统名称
    location = schema.TextLine(
            title=_(u"wei zhi"),
        )
    #分系统类别
    freq = schema.Float(
            title=_(u"gongzuo pinlv"),
        )
    pd_upper = schema.Float(
            title=_(u"shang bian pin"),
        )
    pd_lower = schema.Float(
            title=_(u"xia bian pin"),
        )
    num = schema.Int(
            title=_(u"pinlv dian shu"),
        )
    freq_upper = schema.Float(
            title=_(u"pinlv shang xian"),
        )
    freq_lower = schema.Float(
            title=_(u"pinlv xia xian"),
        )
    bw = schema.Float(
            title=_(u"fashe dai kuan"),
        )
    base_power = schema.Float(
            title=_(u"ji pin gong lv"),
        )
    tzlx = schema.TextLine(
            title=_(u"tiao zhi lei xing"),
        )
    bzf = schema.Float(
            title=_(u"ben zhen pin lv"),
        )
    mid_freq = schema.Float(
            title=_(u"zhong pin"),
        )
    comment1 = schema.TextLine(
            title=_(u"bei zhu"),
        )
class Fashej(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IFashej)

    __tablename__ = 'para_fashej'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('fashej_id_seq'),
            primary_key=True,
            autoincrement=True,
        )

    sbdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    sbmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    pcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    location = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    pd_upper = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    pd_lower = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    num = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )
    freq_upper = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    freq_lower = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    bw = sqlalchemy.schema.Column(sqlalchemy.types.Float(),
            nullable=False,
        )
    base_power = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    tzlx = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    bzf = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    mid_freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    comment1 = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
class IJieshouj(Interface):
    """接收机
    """
    id = schema.Int(
            title=_(u"table primary key"),
        )
    sbdm = schema.TextLine(
            title=_(u"she bei dai ma"),
        )
    sbmc = schema.TextLine(
            title=_(u"jie shou ji ming cheng"),
        )
    pcdm = schema.TextLine(
            title=_(u"zhuang tai pi ci dai ma"),
        )
    location = schema.TextLine(
            title=_(u"wei zhi"),
        )
    fb_upper = schema.Float(
            title=_(u"pin duan shang xian"),
        )
    fb_lower = schema.Float(
            title=_(u"pin duan xia xian"),
        )
    freq = schema.Float(
            title=_(u"gongzuo pinlv"),
        )
    f_upper = schema.Float(
            title=_(u"shang bian pin"),
        )
    f_lower = schema.Float(
            title=_(u"xia bian pin"),
        )
    bw_receiver = schema.Float(
            title=_(u"jie shou ji dai kuan"),
        )
    sen_receiver = schema.Float(
            title=_(u"jie shou ji lin ming du"),
        )
    mf_freq_sign = schema.TextLine(
            title=_(u"zhong pin fu hao"),
        )
    mf_freq = schema.Float(
            title=_(u"zhong pin pin lv"),
        )
    lo_freq = schema.Float(
            title=_(u"ben zhen pin lv"),
        )

class Jieshouj(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IJieshouj)

    __tablename__ = 'para_jieshouj'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('jieshouj_id_seq'),
            primary_key=True,
            autoincrement=True,
        )

    sbdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    sbmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    pcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    location = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    fb_upper = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    fb_lower = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    f_upper = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    f_lower = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    bw_receiver = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    sen_receiver = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    mf_freq_sign = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    mf_freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    lo_freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
class IFashetx(Interface):
    """发射天线
    """
    id = schema.Int(
            title=_(u"table primary key"),
        )
    cssbdm = schema.TextLine(
            title=_(u"cong shu she bei dai ma"),
        )
    cssbmc = schema.TextLine(
            title=_(u"cong shu she bei ming cheng"),
        )
    pcdm = schema.TextLine(
            title=_(u"zhuang tai pi ci dai ma"),
        )
    location = schema.TextLine(
            title=_(u"wei zhi"),
        )
    gain = schema.Float(
            title=_(u"zeng yi"),
        )
    polarization = schema.TextLine(
            title=_(u"ji hua"),
        )
    fwbskd = schema.Float(
            title=_(u"fang wei bo su dai kuan"),
        )
    fybskd = schema.Float(
            title=_(u"fu yang bo su dai kuan"),
        )
    txzxj = schema.Float(
            title=_(u"tian xian zhi xiang jiao"),
        )


class Fashetx(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IFashetx)

    __tablename__ = 'para_fashetx'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('fashetx_id_seq'),
            primary_key=True,
            autoincrement=True,
        )

    cssbdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    cssbmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    pcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    location = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    gain = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    polarization = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    fwbskd = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    fybskd = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    txzxj = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
class IJieshoutx(Interface):
    """接收天线
    """
    id = schema.Int(
            title=_(u"table primary key"),
        )
    cssbdm = schema.TextLine(
            title=_(u"cong shu she bei dai ma"),
        )
    cssbmc = schema.TextLine(
            title=_(u"jie shou tian xian ming cheng"),
        )
    pcdm = schema.TextLine(
            title=_(u"zhuang tai pi ci dai ma"),
        )
    location = schema.TextLine(
            title=_(u"wei zhi"),
        )
    gain = schema.Float(
            title=_(u"zeng yi"),
        )
    polarization = schema.TextLine(
            title=_(u"ji hua"),
        )
    fwbskd = schema.Float(
            title=_(u"fang wei bo su dai kuan"),
        )
    fybskd = schema.Float(
            title=_(u"fu yang bo su dai kuan"),
        )
    txzxj = schema.Float(
            title=_(u"tian xian zhi xiang jiao"),
        )


class Jieshoutx(ORMBase):
    """Database-backed implementation of IJieshoutx
    """
    implements(IJieshoutx)

    __tablename__ = 'para_jieshoutx'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('jieshoutx_id_seq'),
            primary_key=True,
            autoincrement=True,
        )

    cssbdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    cssbmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    pcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    location = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    gain = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    polarization = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    fwbskd = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    fybskd = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    txzxj = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
class ILvboq(Interface):
    """滤波器
    """
    id = schema.Int(
            title=_(u"table primary key"),
        )
    cssbdm = schema.TextLine(
            title=_(u"cong shu she bei dai ma"),
        )
    cssbmc = schema.TextLine(
            title=_(u"lv bo qi ming cheng"),
        )
    pcdm = schema.TextLine(
            title=_(u"zhuang tai pi ci dai ma"),
        )
    location = schema.TextLine(
            title=_(u"wei zhi"),
        )
    freq = schema.Float(
            title=_(u"gong zuo pin lv"),
        )
    f_upper = schema.Float(
            title=_(u"shang bian pin"),
        )
    f_lower = schema.Float(
            title=_(u"xia bian pin"),
        )
    order1 = schema.Float(
            title=_(u"lv bo qi ji shu"),
        )
    s21 = schema.Float(
            title=_(u"lv bo qi cha sun"),
        )

class Lvboq(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(ILvboq)

    __tablename__ = 'para_lvboq'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('lvboq_id_seq'),
            primary_key=True,
            autoincrement=True,
        )

    cssbdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    cssbmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    pcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    location = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    freq = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    f_upper = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    f_lower = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    order1 = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    s21 = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )


class IDianxingtxzyzk(Interface):
    """典型天线增益子库
    """
    id = schema.Int(
            title=_(u"table primary key"),
        )
    type_antennas = schema.TextLine(
            title=_(u"tian xian lei xing"),
        )
    gain = schema.Int(
            title=_(u"zeng yi"),
        )


class Dianxingtxzyzk(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IDianxingtxzyzk)

    __tablename__ = 'para_dianxingtxzyzk'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('dianxingtxzyzk_id_seq'),
            primary_key=True,
            autoincrement=True,
        )

    type_antennas = sqlalchemy.schema.Column(sqlalchemy.types.String(30),
            nullable=False,
        )
    gain = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )


class ITianxianzk(Interface):
    """天线子库
    """
    id = schema.Int(
            title=_(u"table primary key"),
        )
    lib_code = schema.TextLine(
            title=_(u"zi ku dai ma"),
        )
    lib_name = schema.TextLine(
            title=_(u"zi ku ming cheng"),
        )


class Tianxianzk(ORMBase):
    """Database-backed implementation of ITianxianzk
    """
    implements(ITianxianzk)

    __tablename__ = 'para_tianxianzk'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('tianxianzk_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
    lib_code = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    lib_name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )


class IJieshoujzk(Interface):
    """接收机子库
    """
    id = schema.Int(
            title=_(u"table primary key"),
        )
    lib_code = schema.TextLine(
            title=_(u"zi ku dai ma"),
        )
    lib_name = schema.TextLine(
            title=_(u"zi ku ming cheng"),
        )


class Jieshoujzk(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IJieshoujzk)

    __tablename__ = 'para_jieshoujzk'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('jieshoujzk_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
    lib_code = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    lib_name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )


class IFashejzk(Interface):
    """发射机子库
    """
    id = schema.Int(
            title=_(u"table primary key"),
        )
    lib_code = schema.TextLine(
            title=_(u"zi ku dai ma"),
        )
    lib_name = schema.TextLine(
            title=_(u"zi ku ming cheng"),
        )


class Fashejzk(ORMBase):
    """Database-backed implementation of IFashej
    """
    implements(IFashejzk)

    __tablename__ = 'para_fashejzk'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('fashejzk_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
    lib_code = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    lib_name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
#  add by yanghaa for other datebase templates comment to help nav
# 测试实验室start
class ICeshishysh(Interface):
    """测试实验室
    """
    id = schema.Int(
            title=_(u"talbe primary key")
        )
    name = schema.TextLine(
            title=_(u"ming cheng")
        )
    unit = schema.TextLine(
            title=_(u"dan wei")
        )
    level1 = schema.TextLine(
            title=_(u"ji bie")
        )
    survey = schema.TextLine(
            title=_(u"gai kuang")
        )

class Ceshishysh(ORMBase):
    """Database-backed implementation of ICeshishysh
    """
    implements(ICeshishysh)

    __tablename__ = 'test_ceshishysh'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('ceshishysh_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
    name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    unit = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    level1 = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    survey = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
# 测试实验室end

# 测试人员start
class ICeshiry(Interface):
    """测试人员
    """
    id = schema.Int(
            title=_(u"talbe primary key")
        )
    name = schema.TextLine(
            title=_(u"xing ming")
        )
    sex = schema.TextLine(
            title=_(u"xing bie")
        )
    age = schema.Int(
            title=_(u"nian ling")
        )
    edu_level = schema.TextLine(
            title=_(u"xue li")
        )
    post = schema.TextLine(
            title=_(u"zhi cheng")
        )
    certificate_code = schema.TextLine(
            title=_(u"zheng shu bian hao")
        )
    unit = schema.TextLine(
            title=_(u"dan wei")
        )

class Ceshiry(ORMBase):
    """Database-backed implementation of ICeshiry
    """
    implements(ICeshiry)

    __tablename__ = 'test_ceshiry'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('ceshiry_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
    name = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    sex = sqlalchemy.schema.Column(sqlalchemy.types.String(2),
            nullable=False,
        )
    age = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )
    edu_level = sqlalchemy.schema.Column(sqlalchemy.types.String(8),
            nullable=False,
        )
    post = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    certificate_code = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    unit = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
# 测试人员end

# 测试方法start
class ICeshiff(Interface):
    """测试方法
    """
    id = schema.Int(
            title=_(u"talbe primary key")
        )
    m_id = schema.TextLine(
            title=_(u"fang fa bian hao")
        )
    m_title = schema.TextLine(
            title=_(u"fang fa biao ti")
        )
    range1 = schema.TextLine(
            title=_(u"shi yong fan wei")
        )
    device = schema.TextLine(
            title=_(u"yi qi she bei")
        )
#     diagram = schema.TextLine(
#             title=_(u"ce shi kuang tu")
#         )
    step = schema.TextLine(
            title=_(u"ce shi bu zhou")
        )
    annotation = schema.TextLine(
            title=_(u"fu zhu")
        )

class Ceshiff(ORMBase):
    """Database-backed implementation of ICeshiff
    """
    implements(ICeshiff)

    __tablename__ = 'test_ceshiff'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('ceshiff_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
    m_id = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    m_title = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    range1 = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    device = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
#     diagram = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
#             nullable=False,
#         )
    step = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    annotation = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
# 测试方法end

# 测试报告start
class ICeshibg(Interface):
    """测试报告
    """
    id = schema.Int(
            title=_(u"talbe primary key")
        )
    t_id = schema.TextLine(
            title=_(u"ce shi zheng shu bian hao")
        )
    bailor = schema.TextLine(
            title=_(u"wei tuo fang")
        )
    address = schema.TextLine(
            title=_(u"wei tuo fang di zhi")
        )
    device = schema.TextLine(
            title=_(u"bei ce jian")
        )
    eut_id = schema.TextLine(
            title=_(u"EUT bian hao")
        )
    eut_type = schema.TextLine(
            title=_(u"EUT xing hao")
        )
    manufacturor = schema.TextLine(
            title=_(u"zhi zao shang")
        )
    t_date = schema.Date(
            title=_(u"ce shi ri qi")
        )
    t_address = schema.TextLine(
            title=_(u"ce shi di dian")
        )
    t_device = schema.TextLine(
            title=_(u"ce shi she bei")
        )
    t_device_type = schema.TextLine(
            title=_(u"ce shi she bei xing hao")
        )
    t_device_id = schema.TextLine(
            title=_(u"ce shi she bei bian hao")
        )
    reference = schema.TextLine(
            title=_(u"ce shi yi ju")
        )
    temp = schema.Float(
            title=_(u"wen du")
        )
    huminitily = schema.Float(
            title=_(u"shi du")
        )
    t_man = schema.TextLine(
            title=_(u"ce shi ren yuan")
        )
    signer = schema.TextLine(
            title=_(u"qian fa ren")
        )
    assessor = schema.TextLine(
            title=_(u"shen he ren")
        )
    t_result = schema.TextLine(
            title=_(u"ce shi jie guo")
        )

class Ceshibg(ORMBase):
    """Database-backed implementation of ICeshibg
    """
    implements(ICeshibg)

    __tablename__ = 'test_ceshibg'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('ceshibg_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
    t_id = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    bailor = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    address = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    device = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    eut_id = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    eut_type = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    manufacturor = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    t_date = sqlalchemy.schema.Column(sqlalchemy.types.Date(),
            nullable=False,
        )
    t_address = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    t_device = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    t_device_type = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    t_device_id = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    reference = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    temp = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='3,1'),
            nullable=False,
        )
    huminitily = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='2,1'),
            nullable=False,
        )
    t_man = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    signer = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    assessor = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    t_result = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
# 测试报告end

# 测试项目start
class ICeshixm(Interface):
    """测试项目
    """
    id = schema.Int(
            title=_(u"talbe primary key")
        )
    device = schema.TextLine(
            title=_(u"bei ce jian")
        )
    name = schema.TextLine(
            title=_(u"xiang mu ming cheng")
        )
#     diagram = schema.TextLine(
#             title=_(u"shi yi tu")
#         )
    t_remark = schema.TextLine(
            title=_(u"ce shi shuo ming")
        )
    t_strument = schema.TextLine(
            title=_(u"ce shi yi qi")
        )
    t_value = schema.TextLine(
            title=_(u"ce shi shu ju")
        )
    t_result = schema.TextLine(
            title=_(u"ce shi jie guo")
        )

class Ceshixm(ORMBase):
    """Database-backed implementation of ICeshibxm
    """
    implements(ICeshixm)

    __tablename__ = 'test_ceshixm'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('ceshixm_id_seq'),
            primary_key=True,
            autoincrement=True,
        )

    device = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
#     diagram = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
#             nullable=False,
#         )
    t_remark = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    t_strument = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    t_value = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    t_result = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
# 测试项目end

# 靶场start
class IBachang(Interface):
    """靶场 """
    id = schema.Int(
            title=_(u"talbe primary key")
        )
    name = schema.TextLine(
            title=_(u"ba chang ming cheng")
        )
    bcdm = schema.TextLine(
            title=_(u"ba chang dai ma")
        )
    location = schema.TextLine(
            title=_(u"ba chang wei zhi")
        )
    length = schema.Float(
            title=_(u"ba chang chang du")
        )
    width = schema.Float(
            title=_(u"ba chang kuan du")
        )
    wk = schema.Int(
            title=_(u"zhe dang wu ge shu")
        )
    ti = schema.Int(
            title=_(u"gu you fa she ji shu")
        )
    landform = schema.TextLine(
            title=_(u"ba chang di xing tiao jian")
        )
    xh = schema.TextLine(
            title=_(u"ba chang shi he xing hao")
        )
    
    
class Bachang(ORMBase):
    """Database-backed implementation of IBachang
    """
    implements(IBachang)

    __tablename__ = 'envi_bachang'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('bachang_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
    name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    bcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    location = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    length = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    width = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    wk = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )
    ti = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )
    landform = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    xh = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )    
# 靶场end

# 靶场遮挡物start
class IBachangzhdw(Interface):
    """靶场遮挡物    
    """
    id = schema.Int(
            title=_(u"talbe primary key")
        )
    bcdm = schema.TextLine(
            title=_(u"ba chang dai ma")
        )
    shelter_name = schema.TextLine(
            title=_(u"zhe dang wu ming cheng")
        )
#     zdno = schema.Int(
#             title=_(u"xiang mu ming cheng")
#         )
    lu_x = schema.Float(
            title=_(u"zuo shang x zuo biao")
        )
    lu_y = schema.Float(
            title=_(u"zuo shang y zuo biao")
        )
    lu_z = schema.Float(
            title=_(u"zuo shang z zuo biao")
        )
    ld_x = schema.Float(
            title=_(u"zuo xia x zuo biao")
        )
    ld_y = schema.Float(
            title=_(u"zuo xia y zuo biao")
        )
    ld_z = schema.Float(
            title=_(u"zuo xia z zuo biao")
        )
    ru_x = schema.Float(
            title=_(u"you shang x zuo biao")
        )
    ru_y = schema.Float(
            title=_(u"you shang y zuo biao")
        )
    ru_z = schema.Float(
            title=_(u"you shang z zuo biao")
        )
    rd_x = schema.Float(
            title=_(u"you xia x zuo biao")
        )                                    
    rd_y = schema.Float(
            title=_(u"you xia x zuo biao")
        )
    rd_z = schema.Float(
            title=_(u"you xia x zuo biao")
        )


class Bachangzhdw(ORMBase):
    """Database-backed implementation of IBachangzhdw
    """
    implements(IBachangzhdw)

    __tablename__ = 'envi_bachangzhdw'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('bachangzhdw_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
    bcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    shelter_name = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
#     zdno = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
#             nullable=False,
#         )
    lt_x = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    lt_y = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    lt_z = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    ld_x = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    ld_y = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    ld_z = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    rt_x = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    rt_y = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    rt_z = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    rd_x = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    rd_y = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    rd_z = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
            
# 测试项目end

# 靶场发射机的电磁特性start
class IBachangfshj(Interface):
    """靶场发射机
    """
    id = schema.Int(
            title=_(u"talbe primary key")
        )
    bcdm = schema.Int(
            title=_(u"ba chang dai ma")
        )
    sbmc = schema.TextLine(
            title=_(u"fa she ji ming cheng")
        )
    fsno = schema.Int(
            title=_(u"fa she ji xu hao")
        )
    x = schema.Float(
            title=_(u"ba chang x zuo biao")
        )
    y = schema.Float(
            title=_(u"ba chang y zuo biao")
        )
    z = schema.Float(
            title=_(u"ba chang z zuo biao")
        )                
    ft = schema.TextLine(
            title=_(u"gong zuo pin lv")
        )
    pd_u = schema.Float(
            title=_(u"shang bian pin")
        )
    pd_l = schema.Float(
            title=_(u"xia bian pin")
        )
    num = schema.Int(
            title=_(u"pin lv dian shu")
        )
    fu = schema.Float(
            title=_(u"pin duan shang xian")
        )
    fl = schema.Float(
            title=_(u"pin duan xia xian")
        )
    bt = schema.Float(
            title=_(u"fa she dai kuan")
        )
    pt = schema.Float(
            title=_(u"ji pin gong lv")
        )                        
    tzlx = schema.TextLine(
            title=_(u"tiao zhi lei xing")
        )
    bzf = schema.Float(
            title=_(u"ben zheng pin lv")
        )
    zp = schema.Float(
            title=_(u"zhong pin")
        )
    bz = schema.TextLine(
            title=_(u"bei zhu")
        )    

class Bachangfshj(ORMBase):
    """Database-backed implementation of IBachangfshj
    """
    implements(IBachangfshj)

    __tablename__ = 'envi_bachangfshj'

    id = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),Sequence('bachangfshj_id_seq'),
            primary_key=True,
            autoincrement=True,
        )
    bcdm = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    sbmc = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=False,
        )
    fsno = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )
    x = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    y = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    z = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    ft = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    pt_u = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    pt_l = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    num = sqlalchemy.schema.Column(sqlalchemy.types.Integer(),
            nullable=False,
        )
    fu = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=True,
        )
    fl = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=True,
        )
    bt = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    pt = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    tzlx = sqlalchemy.schema.Column(sqlalchemy.types.String(16),
            nullable=False,
        )
    bzf = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    zp = sqlalchemy.schema.Column(sqlalchemy.types.Float(precision='16,4'),
            nullable=False,
        )
    bz = sqlalchemy.schema.Column(sqlalchemy.types.String(32),
            nullable=True,
        )                                     
# 测试项目end
