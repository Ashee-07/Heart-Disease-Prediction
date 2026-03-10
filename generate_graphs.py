import matplotlib.pyplot as plt
import os

def generate_accuracy_graph():
    models = ['Logistic Regression', 'Naive Bayes', 'Random Forest', 'XGBoost', 'KNN', 'Decision Tree', 'SVM']
    accuracies = [0.78, 0.78, 0.79, 0.73, 0.82, 0.79, 0.78]

    plt.figure(figsize=(10, 6))
    plt.bar(models, accuracies, color=['#3498db', '#9b59b6', '#e67e22', '#e74c3c', '#2ecc71', '#1abc9c', '#34495e'])
    plt.xlabel('Models')
    plt.ylabel('Accuracy')
    plt.title('Comparison of Model Accuracies')
    plt.ylim(0, 1.0)
    for i, v in enumerate(accuracies):
        plt.text(i, v + 0.02, str(v), ha='center', fontweight='bold')
    
    static_dir = os.path.join('static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    plt.savefig(os.path.join(static_dir, 'accuracy_comparison.png'))
    print("Graph saved to static/accuracy_comparison.png")

if __name__ == "__main__":
    generate_accuracy_graph()
