For this application you need to insall a few packs for python:

pandas: pip install pandas
spacy: pip install spacy
scikit-learn: pip install scikit-learn
tkinter: pip install tkinter (usually comes pre-installed with Python)
pillow: pip install pillow (PIL, the Python Imaging Library)

Please note that spacy requires additional language models to be installed separately. 
Command: python -m spacy download sv.

There are two rows where you need to add your path to specific documents. NOTE that you add to backslashes to the path as in the examples.
For the  Cleaned_file.csv row 13:
Example: data = pd.read_csv("C:\\Users\\User\\Download\\Cleaned_file.csv")

For the image row 86:
Example:image= Image.open("C:\\Users\\User\\Download\\NMF.jpg")

