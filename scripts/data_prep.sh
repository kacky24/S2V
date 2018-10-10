
NUM_WORDS=20001
OUTPUT_DIR="../src/data/TFRecords" 
VOCAB_FILE="../src/data/dictionary.txt"  
TOKENIZED_FILES="../src/data/txt_tokenized/*"

python ../src/data/preprocess_dataset.py \
  --input_files "$TOKENIZED_FILES" \
  --output_dir $OUTPUT_DIR \
  --num_words $NUM_WORDS \
  --max_sentence_length 50 \
  --case_sensitive



#   --vocab_file $VOCAB_FILE \
