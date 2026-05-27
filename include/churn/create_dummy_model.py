"""
Create a dummy model for testing the streaming pipeline
"""
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Create a simple dummy model
model = RandomForestClassifier(n_estimators=10, random_state=42)

# Create some dummy training data
X_dummy = np.random.rand(100, 50)  # 100 samples, 50 features
y_dummy = np.random.randint(0, 2, 100)  # Binary classification

# Train the model
model.fit(X_dummy, y_dummy)

# Define feature columns (these should match what the feature engine generates)
feature_columns = [
    # Time window features
    '1h_total_events', '1h_support_calls', '1h_billing_issues', '1h_complaints', '1h_payment_failures',
    '1h_usage_spikes', '1h_usage_drops', '1h_usage_volatility', '1h_total_purchases', '1h_purchase_amount',
    '1h_avg_purchase_amount', '1h_login_frequency', '1h_session_ratio', '1h_negative_event_ratio', '1h_avg_call_duration',
    
    '24h_total_events', '24h_support_calls', '24h_billing_issues', '24h_complaints', '24h_payment_failures',
    '24h_usage_spikes', '24h_usage_drops', '24h_usage_volatility', '24h_total_purchases', '24h_purchase_amount',
    '24h_avg_purchase_amount', '24h_login_frequency', '24h_session_ratio', '24h_negative_event_ratio', '24h_avg_call_duration',
    
    '7d_total_events', '7d_support_calls', '7d_billing_issues', '7d_complaints', '7d_payment_failures',
    '7d_usage_spikes', '7d_usage_drops', '7d_usage_volatility', '7d_total_purchases', '7d_purchase_amount',
    '7d_avg_purchase_amount', '7d_login_frequency', '7d_session_ratio', '7d_negative_event_ratio', '7d_avg_call_duration',
    
    # Current event features
    'current_event_type_support_call', 'current_event_type_billing_issue', 'current_event_type_complaint', 'current_event_type_payment_failed',
    
    # Customer profile features
    'tenure_months', 'monthly_charges', 'contract_month_to_month', 'contract_one_year', 'contract_two_year'
]

# Save the model
with open('/home/magicdash/astro-airflow/include/churn/models/churn_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save metadata
metadata = {
    'feature_columns': feature_columns,
    'model_type': 'RandomForestClassifier',
    'version': '1.0.0',
    'created_for': 'streaming_testing'
}

with open('/home/magicdash/astro-airflow/include/churn/models/model_metadata.pkl', 'wb') as f:
    pickle.dump(metadata, f)

print("Created dummy model and metadata files")
print(f"Feature columns: {len(feature_columns)}")