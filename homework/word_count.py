"""Taller evaluable"""

import os
import glob
import pandas as pd  # type: ignore
import re


def run_job(input_directory, output_directory):
    """Job"""

    files = glob.glob(os.path.join(input_directory, "*.txt"))
    words = []

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                # Eliminar puntuación y pasar a minúsculas
                clean_line = re.sub(r"[^\w\s]", "", line.lower())
                line_words = clean_line.strip().split()
                words.extend(line_words)

    df = pd.DataFrame(words, columns=["word"])
    word_counts = df.value_counts().reset_index(name="count")

    if os.path.exists(output_directory):
        for f in glob.glob(os.path.join(output_directory, "*")):
            os.remove(f)
    else:
        os.makedirs(output_directory)

    output_file = os.path.join(output_directory, "part-00000")
    word_counts.to_csv(output_file, sep="\t", index=False, header=False)

    with open(os.path.join(output_directory, "_SUCCESS"), "w", encoding="utf-8") as f:
        f.write("")
