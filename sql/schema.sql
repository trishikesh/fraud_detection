-- PostgreSQL schema for processed PaySim fraud analytics dataset.
DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
    step INTEGER,
    amount DOUBLE PRECISION,
    oldbalanceOrg DOUBLE PRECISION,
    newbalanceOrig DOUBLE PRECISION,
    oldbalanceDest DOUBLE PRECISION,
    newbalanceDest DOUBLE PRECISION,
    isFraud INTEGER,
    isFlaggedFraud INTEGER,
    hour INTEGER,
    type_CASH_IN BOOLEAN,
    type_CASH_OUT BOOLEAN,
    type_DEBIT BOOLEAN,
    type_PAYMENT BOOLEAN,
    type_TRANSFER BOOLEAN,
    high_value_transaction BOOLEAN,
    balance_error_orig DOUBLE PRECISION,
    balance_error_dest DOUBLE PRECISION
);
