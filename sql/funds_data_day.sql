CREATE TABLE IF NOT EXISTS public.fund_daily_data (
    id            bigserial     NOT NULL,
    code          varchar(32)   NOT NULL, --基金代码
    date          date          NOT NULL, --日期
    nav           numeric       NOT NULL,
    jj_lggz       numeric       NOT NULL,
    growth_rate   numeric       NOT NULL,
    subscription_status varchar(64) NOT NULL,
    redemption_status   varchar(64) NOT NULL,
    dividends     varchar(128) DEFAULT '',
    create_time   timestamp without time zone NOT NULL DEFAULT now(),

    PRIMARY KEY (code, date)
);

CREATE TABLE IF NOT EXISTS public.fund_estimation (
    id      bigserial  NOT NULL,
    code    varchar(32) NOT NULL,
    gsz     numeric     NOT NULL, --实时估算净值
    gszzl   numeric     NOT NULL, --实时增幅
    gztime        timestamp without time zone   NOT NULL, --估算时间
    create_time   timestamp without time zone   NOT NULL DEFAULT now(),
    
    PRIMARY KEY (code, gztime)
)
