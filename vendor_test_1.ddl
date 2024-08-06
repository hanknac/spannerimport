CREATE TABLE vendor_test_1 (
    vendor_id UUID NOT NULL,
    vendor_number STRING(100) NOT NULL,
    display_name STRING(500) NOT NULL,
    created_by STRING(100) NOT NULL,
    created_timestamp_utc timestamp,
) PRIMARY KEY (vendor_id)
