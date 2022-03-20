'''
@Time    : 2021/1/24 15:57
@Author  : 19045845
'''
import argparse
from tspider.commands.entrance import ENTRANCEDICT


def parse_args():
    parser = argparse.ArgumentParser(description="download")
    parser.add_argument("--proxies", type=bool, default=False)
    parser.add_argument("--name", type=str, default="ace_promoteMarketing",
                        choices=["dpa", "goods", "qiantu", "shetu", "mizhi", "gaoding", "burst", "kaboompics", "negativespace",
                                 "freestocks", "pexels", "gaoding_product_main_image", "tusiji_main_image", "tusiji_detail_image",
                                 "canva_poster", "JD_linglong", "tuguaishou_poster", "qiantu_banner", "ace_socialPoster",
                                 "ace_atmosphere", "artstore", "ued", "ace_promoteMarketing"])
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    ENTRANCEDICT.get(args.name)(args)
