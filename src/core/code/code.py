from enum import Enum


class BaseCode(Enum):
    @classmethod
    def to_dict(cls):
        # 전체 이넘 타입 dictionary로 변환
        return {enum_type.name: enum_type.value for enum_type in cls}


class SignUpType(BaseCode):
    NORMAL      = {"code": "1", "name": "일반회원가입"}
    GOOGLE      = {"code": "2", "name": "구글회원가입"}
    FACEBOOK    = {"code": "3", "name": "페이스북회원가입"}
    KAKAO       = {"code": "4", "name": "카카오회원가입"}
    TWITTER     = {"code": "5", "name": "트위터회원가입"}


# 작가 상태코드(승인대기: 1, 일반: 2, 블랙: 3, 작가등록취소: 4)
class ArtistStatusCode(BaseCode):
    WAITING     = {"code": "1", "name": "승인대기"}
    NORMAL      = {"code": "2", "name": "일반"}
    BLACK       = {"code": "3", "name": "블랙"}
    CANCEL      = {"code": "4", "name": "작가등록취소"}


# 작가 구분코드(일반=N, 사업자=C)
class ArtistTypeCode(BaseCode):
    NORMAL      = {"code": "N", "name": "일반"}
    CORPORATION = {"code": "C", "name": "사업자"}


class IsTopYn(BaseCode):
    Y = {"code": "Y", "name": "고정함"}
    N = {"code": "N", "name": "고정안함"}


class IsUseYn(BaseCode):
    Y = {"code": "Y", "name": "사용"}
    N = {"code": "N", "name": "미사용"}


class NoticeTypeCode(BaseCode):
    # 알림 타입 코드(K=Kakao, E=Email, B=Background, P=Push)
    PUSH        = {"code": "1", "name": "Push"}
    EMAIL       = {"code": "2", "name": "Email"}
    KAKAO       = {"code": "3", "name": "Kakao"}
    BACKGROUND  = {"code": "4", "name": "Background"}


class NoticeStatusCode(BaseCode):
    # 알림 상태코드(R=준비, S=성공, F=실패)
    READY       = {"code": "R", "name": "준비"}
    SUCCESS     = {"code": "S", "name": "성공"}
    FAIL        = {"code": "F", "name": "실패"}


class TermsTypeCode(BaseCode):
    # 0: 개인정보 처리방침, 1: 서비스 이용약관, 2: 마케팅 수신동의, 3: 온라인 경매약관, 4: 중고거래 운영정책, 5: 위치서비스 이용약관, 6: 작가회원 입점약관
    PRIVACY_POLICY          = {"code": "0", "name": "개인정보 처리방침"}
    SERVICE_TERMS           = {"code": "1", "name": "서비스 이용약관"}
    MARKETING_AGREE         = {"code": "2", "name": "마케팅 수신동의"}
    ONLINE_AUCTION_TERMS    = {"code": "3", "name": "온라인 경매약관"}
    USED_TRADE_POLICY       = {"code": "4", "name": "중고거래 운영정책"}
    LOCATION_SERVICE_TERMS  = {"code": "5", "name": "위치서비스 이용약관"}
    AUTHOR_TERMS            = {"code": "6", "name": "작가회원 입점약관"}


class TermsStatusCode(BaseCode):
    # 0: 적용예정, 1: 공지중, 2: 종료
    APPLYING    = {"code": "0", "name": "적용예정"}
    NOTICE      = {"code": "1", "name": "공지중"}
    END         = {"code": "2", "name": "종료"}


class TermsUserTypeCode(BaseCode):
    # Normal: N, Artist: A, Corporation Artist: C
    NORMAL      = {"code": "N", "name": "일반회원"}
    ARTIST      = {"code": "A", "name": "작가"}
    CORPORATION = {"code": "C", "name": "법인작가"}


class GroupTypeCode(BaseCode):
    # 0: 작가, 1: 일반회원
    MANAGER     = {"code": "0", "name": "관리자"}
    USER        = {"code": "1", "name": "일반회원"}


class AuthorityTypeCode(BaseCode):
    # 쓰기=W, 읽기=R, 차단=D
    WRITE       = {"code": "W", "name": "쓰기"}
    READ        = {"code": "R", "name": "읽기"}
    BLOCK       = {"code": "D", "name": "차단"}


class ApprovalStatusCode(BaseCode):
    # 승인 상태(0: 미승인, 1: 승인완료, 2: 반려, 3: 재승인요청)
    WAITING     = {"code": "0", "name": "미승인"}
    APPROVED    = {"code": "1", "name": "승인완료"}
    REJECTED    = {"code": "2", "name": "반려"}
    REAPPROVAL  = {"code": "3", "name": "재승인요청"}


class ProductSaleTypeCode(BaseCode):
    # 상품 판매종류 코드(A(Auction): 경매, N(Normal): 일반판매)
    AUCTION     = {"code": "A", "name": "경매"}
    NORMAL      = {"code": "N", "name": "일반판매"}


class ProductStatusTypeCode(BaseCode):
    # 상품 판매상태(P(Pause): 일시중지, I(Ing): 판매중, F(Finished): 판매완료, D(Denied): 판매정지)
    PAUSE       = {"code": "P", "name": "일시중지"}
    ING         = {"code": "I", "name": "판매중"}
    FINISHED    = {"code": "F", "name": "판매완료"}
    DENIED      = {"code": "D", "name": "판매정지"}


class ShippingMethodTypeCode(BaseCode):
    # 배송 가능 코드 목록(1: 착불, 2: 배송비 안내, 3: 직접수령)
    UNPAID      = {"code": "1", "name": "착불"}
    COST_SET    = {"code": "2", "name": "배송비 안내"}
    DIRECT      = {"code": "3", "name": "직접수령"}


# hash_tag_01_type_code > 해쉬태드 1Depth(1: #회화, 2: #동양화, 3: #조소/공예, 4: #포토그래픽, 5: #섬유/패션, 6: #디지털아트, 7: #가구/조명, 8: #기타)
class HashTag01TypeCode(BaseCode):
    PAINTING    = {"code": "1", "name": "#회화"}
    ORIENTAL    = {"code": "2", "name": "#동양화"}
    SCULPTURE   = {"code": "3", "name": "#조소/공예"}
    PHOTOGRAPHY = {"code": "4", "name": "#포토그래픽"}
    FASHION     = {"code": "5", "name": "#섬유/패션"}
    DIGITAL     = {"code": "6", "name": "#디지털아트"}
    FURNITURE   = {"code": "7", "name": "#가구/조명"}
    ETC         = {"code": "8", "name": "#기타"}


# hash_tag_02_type_code > 해쉬태드 2Depth(1: #순수예술, 2: #디자인)
class HashTag02TypeCode(BaseCode):
    ART         = {"code": "1", "name": "#순수예술"}
    DESIGN      = {"code": "2", "name": "#디자인"}


# hash_tag_03_type_code > 해쉬태드 3Depth(1: #유형(실물), 2: #무형(비실물))
class HashTag03TypeCode(BaseCode):
    REAL        = {"code": "1", "name": "#유형(실물)"}
    UNREAL      = {"code": "2", "name": "#무형(비실물)"}


# - 결제유형(1: 신용카드, 2: 카카오페이, 3: 무통장결제)
class PaymentTypeCode(BaseCode):
    CREDIT      = {"code": "1", "name": "신용카드"}
    KAKAO       = {"code": "2", "name": "카카오페이"}
    BANK        = {"code": "3", "name": "무통장결제"}


# - 결제상태(1: 결제대기, 2: 결제완료, 3: 결제취소)
class PaymentStatusTypeCode(BaseCode):
    WAITING     = {"code": "1", "name": "결제대기"}
    COMPLETE    = {"code": "2", "name": "결제완료"}
    CANCEL      = {"code": "3", "name": "결제취소"}


# 상품유형(product_type_code)(경매, 굿즈, 리셀)
class ProductTypeCode(BaseCode):
    AUCTION     = {"code": "A", "name": "경매"}
    GOODS       = {"code": "G", "name": "굿즈"}
    RESELL      = {"code": "R", "name": "리셀"}


# 정산 상태코드(1: 대기, 2: 완료, 3: 취소)
class SettlementStatusTypeCode(BaseCode):
    WAITING     = {"code": "1", "name": "대기"}
    COMPLETE    = {"code": "2", "name": "완료"}
    CANCEL      = {"code": "3", "name": "취소"}


# 배송상태(shipping_status_type_code)
class ShippingStatusTypeCode(BaseCode):
    WAITING     = {"code": "1", "name": "배송대기"}
    COMPLETE    = {"code": "2", "name": "배송완료"}
    CANCEL      = {"code": "3", "name": "배송취소"}


# 배송타입(shipping_type_code)(1: 착불, 2: 배송비 안내, 3: 직접수령)
class ShippingTypeCode(BaseCode):
    UNPAID      = {"code": "1", "name": "착불"}
    COST_SET    = {"code": "2", "name": "배송비 안내"}
    DIRECT      = {"code": "3", "name": "직접수령"}


# 환불상태(1: 환불대기, 2: 환불완료, 3: 환불취소)
class RefundStatusTypeCode(BaseCode):
    WAITING     = {"code": "1", "name": "환불대기"}
    COMPLETE    = {"code": "2", "name": "환불완료"}
    CANCEL      = {"code": "3", "name": "환불취소"}


# 유저 상태 코드(N=일반, D=휴면(dormancy), B=블랙)
class UserStatusTypeCode(BaseCode):
    NORMAL      = {"code": "N", "name": "일반"}
    DORMANCY    = {"code": "D", "name": "휴면"}
    BLACK       = {"code": "B", "name": "블랙"}


# 유저 성별(M=남자, F=여자)
class GenderTypeCode(BaseCode):
    MALE        = {"code": "M", "name": "남자"}
    FEMALE      = {"code": "F", "name": "여자"}


class CooperationStatusTypeCode(BaseCode):
    WAITING     = {"code": "1", "name": "대기중"}
    ING         = {"code": "2", "name": "진행중"}
    FINISHED    = {"code": "3", "name": "종료"}