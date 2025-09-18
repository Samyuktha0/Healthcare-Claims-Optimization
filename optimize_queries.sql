CREATE INDEX idx_amount ON claims(amount);
SELECT diagnosis_code, COUNT(*) FROM claims GROUP BY diagnosis_code;
