from selene_sdk.utils import load_path
from selene_sdk.utils import parse_configs_and_run


configs = load_path("./pATM_hg19_blacklist_train.yml")
parse_configs_and_run(configs, lr=0.01)

configs = load_path("./pATM_h19_blacklist_AsiSI_masked_train.yml")
parse_configs_and_run(configs, lr=0.01)



configs = load_path("./53BP1_hg19_blacklist_train.yml")
parse_configs_and_run(configs, lr=0.01)


configs = load_path("./53BP1_h19_blacklist_AsiSI_masked_train.yml")
parse_configs_and_run(configs, lr=0.01)
