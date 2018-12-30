from textgenrnn import textgenrnn
textgen = textgenrnn('model')
textgen.generate(1, temperature=1.2)