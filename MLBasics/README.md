## Machine Learning Introduction

### Module 1: Introduction to Prediction

-   **Understanding Prediction:**

    > Prediction in machine learning is about forecasting an outcome based on input data. For example, predicting house prices based on features like location, size, and number of bedrooms.

-   **Why Prediction is Important:**

    > Predictions help in decision-making, understanding trends, and optimizing processes. They are used in various fields like finance, healthcare, marketing, and more.

-   **Logic Building Without Code:**
    > Before diving into coding, it’s essential to understand the logic behind prediction. Think about how you would make a prediction manually. For example, if predicting house prices, consider factors like location, size, age, and compare similar houses. This helps in understanding the relationships between input features and the output.

### Module 2: Data Exploration with Pandas

-   **Basic Data Exploration:**

    > Data exploration is the first step in data analysis. It involves understanding the structure, content, and relationships within the data.

-   **Using Pandas Library:**

    > Pandas is a powerful library in Python for data manipulation and analysis. It provides data structures like DataFrame to handle data efficiently.

-   **Key Commands:**

    -   **`head()`**: Displays the first few rows of the DataFrame, giving a quick glimpse of the data.

        ```python
        import pandas as pd
        df = pd.read_csv('data.csv')
        print(df.head())
        ```

    -   **`read_csv()`**: Loads data from a CSV file into a DataFrame.

        ```python
        df = pd.read_csv('data.csv')
        ```

    -   **`describe()`**: Generates descriptive statistics, summarizing the central tendency, dispersion, and shape of the dataset’s distribution.

        ```python
        print(df.describe())
        ```

    -   **Additional Commands**: Other useful commands include `info()`, `shape`, `columns`, etc., to get more information about the data.
        ```python
        print(df.info())
        print(df.shape)
        print(df.columns)
        ```

### Module 3: Building the First Model

-   **Introduction to Model Creation:**

    > A model in machine learning is a mathematical representation of a real-world process. It learns from data to make predictions.

-   **Using DecisionTreeRegressor:**

    > DecisionTreeRegressor is a model from the `sklearn` library used for regression tasks. It splits the data into subsets based on feature values to make predictions.

    **The Process:**

    1. **Importing Libraries and Data:**

        ```python
        from sklearn.tree import DecisionTreeRegressor
        import pandas as pd

        df = pd.read_csv('data.csv')
        ```

    2. **Preparing Features and Target Variable:**

        ```python
        X = df[['feature1', 'feature2', 'feature3']]  # Replace with actual feature names
        y = df['target']  # Replace with actual target variable name
        ```

    3. **Creating and Training the Model:**

        ```python
        model = DecisionTreeRegressor()
        model.fit(X, y)
        ```

    4. **Making Predictions:**

        ```python
        predictions = model.predict(X)
        ```

### Module 4: Model Validation

-   **Importance of Model Validation:**

    > Validation is crucial to ensure that the model performs well on unseen data, not just the training data. It helps in assessing the model's generalizability.

-   **Calculating Mean Absolute Error:**

    -   Mean Absolute Error (MAE) measures the average magnitude of errors in predictions, without considering their direction. It’s a straightforward way to understand prediction accuracy.

        ```python
        from sklearn.metrics import mean_absolute_error

        mae = mean_absolute_error(y, predictions)
        print('Mean Absolute Error:', mae)
        ```

-   **Using train_test_split:**

    -   Splitting the dataset into training and validation sets helps in assessing the model’s performance on unseen data. `train_test_split` from `sklearn.model_selection` is commonly used for this purpose.

        ```python
        from sklearn.model_selection import train_test_split

        X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=0)
        model.fit(X_train, y_train)
        predictions = model.predict(X_valid)
        mae = mean_absolute_error(y_valid, predictions)
        print('Validation MAE:', mae)
        ```

### Module 5: Underfitting and Overfitting

-   **Overfitting**

    > When a machine learning model learns the training data too well, including its noise and outliers, it performs very well on training data but poorly on new, unseen data. This happens because the model becomes too complex and "memorizes" rather than generalizes, capturing specific details rather than broader patterns.

-   **Underfitting**

    > When a model is too simple, it fails to capture the underlying patterns in the training data. It performs poorly on both the training and test data, as it cannot represent the complexity of the data, often due to a lack of features or insufficient training.

-   **Solution**

    We need to find the best number of leafs, such that the MAE for our model is on the lower side, of the overfitted graph as shown here ![](https://storage.googleapis.com/kaggle-media/learn/images/AXSEOfI.png)

    ```python
    def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
        model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
        model.fit(train_X, train_y)
        preds_val = model.predict(val_X)
        mae = mean_absolute_error(val_y, preds_val)
        return(mae)
    ```

    Then we can look through with other possible leaf node counts to figure out the perfect tree size for our estimations. In other words, the lead node count that results in the least MAE is the best to be used for our DecisionTreeRegressor

    ```python
    for max_leaf_nodes in [5, 50, 500, 5000]:
        my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
        print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
    ```
