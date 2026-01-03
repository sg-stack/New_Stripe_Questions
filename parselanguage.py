# def parse_accept_language(header, supported_languages):
#     if not header or not supported_languages:
#         return []

#     supported = set(supported_languages)
#     result = []

#     for lang in header.split(","):
#         lang = lang.strip()
#         if lang in supported:
#             result.append(lang)

#     return result
# print(parse_accept_language("en-US",["en-US","fr-Fr"]))
# def parseAccepteLanguage(accept_language_header: str, supported_languages: list[str]) -> list[str]:
#     supported_language_map: dict[str, set[str]] = {}
#     for language in supported_languages:
#         lang, country = language.split("-")
#         if lang not in supported_language_map:
#             supported_language_map[lang] = set()

#         supported_language_map[lang].add(country)
#     print(supported_language_map)
#     results = []
#     for language in accept_language_header.split(" "):
#         lang, country = language.split("-")

#         if lang not in supported_language_map:
#             continue

#         if country not in supported_language_map[lang]:
#             continue

#         results.append(language)

#     return results
# print(parseAccepteLanguage("en-US",["en-US","fr-FR","en-IND"]))