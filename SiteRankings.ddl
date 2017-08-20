CREATE TABLE SiteRankings (
    rankid INT64 NOT NULL,
    domain STRING(100) NOT NULL,
    idndomain STRING(100) NOT NULL,
    idntld STRING(100) NOT NULL,
    prevrank INT64,
    prevrefips INT64,
    prevrefsubnets INT64,
    prevtldrank INT64,
    refips INT64 NOT NULL,
    refsubnets INT64 NOT NULL,
    tld STRING(100) NOT NULL,
    tldrank INT64 NOT NULL,
) PRIMARY KEY (rankid)
