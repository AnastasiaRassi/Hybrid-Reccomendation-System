import os

###################### DATA INGESTION ############################3

RAW_DIR = "data/raw"
CONFIG_PATH = "config/config.yaml"


######################## DATA PROCESSING ##########################

PROCESSED_DIR = "data/processed"
ANIMELIST_CSV = "data/raw/animelist.csv"
ANIME_CSV = "data/raw/anime.csv"
ANIMESYNOPSIS_CSV = "data/raw/anime_with_synopsis.csv"

X_TRAIN_ARRAY = os.path.join(PROCESSED_DIR,"X_train_array.pkl")
X_TEST_ARRAY = os.path.join(PROCESSED_DIR,"X_test_array.pkl")
Y_TRAIN = os.path.join(PROCESSED_DIR,"y_train.pkl")
Y_TEST = os.path.join(PROCESSED_DIR,"y_test.pkl")

RATING_DF = os.path.join(PROCESSED_DIR,"rating_df.csv")
DF = os.path.join(PROCESSED_DIR,"anime_df.csv")
SYNOPSIS_DF = os.path.join(PROCESSED_DIR,"synopsis_df.csv")

USER2USER_ENCODED = "data/processed/user2user_encoded.pkl"
USER2USER_DECODED = "data/processed/user2user_decoded.pkl"

ANIME2ANIME_ENCODED = "data/processed/anim2anime_encoded.pkl"
ANIME2ANIME_DECODED = "data/processed/anim2anime_decoded.pkl"


###################### MODEL TRAINING #######################333

MODEL_DIR = "artifacts/model"
WEIGHTS_DIR = "artifacts/weights"
MODEL_PATH = os.path.join(MODEL_DIR,"model.h5")
ANIME_WEIGHTS_PATH = os.path.join(WEIGHTS_DIR,"anime_weights.pkl")
USER_WEIGHTS_PATH = os.path.join(WEIGHTS_DIR,"user_weights.pkl")
CHECKPOINT_FILE_PATH = "artifacts/model_checkpoint/weights.weights.h5"