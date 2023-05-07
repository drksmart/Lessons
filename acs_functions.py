import pandas as pd

def acs_import(file_path):
    width = [
    1, 2, 8, 9, 16, 8, 1, 1, 3, 20, 15, 6, 6, 1, 28, 10, 2, 28, 4, 2, 4, 10, 28, 2, 5, 1, 8, 28, 10, 2, 28, 4,
    2, 4, 10, 28, 2, 5, 1, 4, 2, 13, 66, 1, 1, 31, 35, 16, 1, 1, 8, 1, 1, 8, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6,
    6, 6, 6, 6, 1, 81, 1]
    headings = [
    'RECORD_TYPE', 'FILE_VERSION', 'SEQ_NUM', 'MAILER_ID', 'KEYLINE', 'MOVE_EFF_DT', 'MOVE_TYPE', 'DEL_CODE',
    'USPS_SITE_ID', 'LAST_NAME', 'FIRST_NAME', 'PREFIX', 'SUFFIX', 'OLD_ADDR_TYPE', 'OLD_URB', 'OLD_PRIM_NUM',
    'OLD_PRE_DIR', 'OLD_STREET_NM', 'OLD_SUFFIX', 'OLD_POST_DIR', 'OLD_UNIT', 'OLD_SECOND_NUM', 'OLD_CITY',
    'OLD_STATE', 'OLD_ZIP', 'NEW_ADDR_TYPE', 'NEW_PMB', 'NEW_URB', 'NEW_PRIM_NUM', 'NEW_PRE_DIR',
    'NEW_STREET_NM', 'NEW_SUFFIX', 'NEW_POST_DIR', 'NEW_UNIT', 'NEW_SECOND_NUM', 'NEW_CITY', 'NEW_STATE',
    'NEW_ZIP', 'NEW_HYPHEN', 'NEW_PLUS', 'NEW_DEL_POINT', 'NEW_ABBR_CITY', 'NEW_ADDR_LABEL', 'FEE_NOT',
    'NOT_TYPE', 'IMB', 'IMPB', 'ID_TAB', 'HARD_E_FLAG', 'ACS_TYPE', 'FULFILL_DT', 'PROCESS_TYPE',
    'CAPTURE_TYPE', 'AVAIL_DT', 'MAIL_SHAPE', 'MAIL_ACTION_CD', 'NIXIE_FLG', 'PROD_CD_A', 'PROD_CD_FEE_A',
    'PROD_CD_B ', 'PROD_CD_FEE_B ', 'PROD_CD_C ', 'PROD_CD_FEE_C ', 'PROD_CD_D ', 'PROD_CD_FEE_D ',
    'PROD_CD_E ', 'PROD_CD_FEE_E ', 'PROD_CD_F ', 'PROD_CD_FEE_F ', 'DPV', 'FILLER', 'END']
    file = pd.read_fwf(file_path, widths=width, header=None, names=headings)
    return file[(file.KEYLINE.str.len() == 11)]


def concat_unique(append_file, base_file):
    to_append = append_file[~append_file['KEYLINE'].isin(base_file['KEYLINE'])]
    return pd.concat([base_file, to_append])

acs1 = acs_import("/Users/dereksmart/Documents/P20520022_829.txt")
acs2 = acs_import("/Users/dereksmart/Documents/P20521022_829.txt")
print(acs1.shape)
print(acs2.shape)

acs_all = concat_unique(acs2, acs1)
print(acs_all.shape)