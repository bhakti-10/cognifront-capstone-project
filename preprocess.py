from sklearn.preprocessing import LabelEncoder,StandardScaler
Encode_list=['online_order','book_table','location','rest_type','cuisines','type','city']

def label_encode_input(df):
    endex = LabelEncoder()
    for x in Encode_list:
        df[x] = endex.fit_transform(df[x])
    return df