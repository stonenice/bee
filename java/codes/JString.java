public class JString {

        public final static String format(String tpl, String json) {
            return new JString(tpl).toString(json);
        }

        public final static String format(String tpl, List<Object> args) {
            return new JString(tpl).toString(args);
        }

        public final static String format(String tpl, Map<String, Object> kwargs) {
            return new JString(tpl).toString(kwargs);
        }

        public final static JString valueOf(String tpl) {
            return new JString(tpl);
        }

        private final static SimpleDateFormat SDF = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

        private String content;

        private String tagPrefix;
        private String tagSuffix;

        public JString(Object obj) {
            this.tagPrefix = "${";
            this.tagSuffix = "}";

            if (obj instanceof String) {
                content = obj.toString();
            } else if (obj instanceof Date) {
                content = SDF.format(obj);
            } else {
                content = "";
            }
        }

        public String getTagPrefix() {
            return tagPrefix;
        }

        public void setTagPrefix(String tagPrefix) {
            this.tagPrefix = tagPrefix;
        }

        public String getTagSuffix() {
            return tagSuffix;
        }

        public void setTagSuffix(String tagSuffix) {
            this.tagSuffix = tagSuffix;
        }

        public boolean neededFill() {
            if (content == null || content.length() <= 0) return false;
            return content.indexOf(tagPrefix) >= 0;
        }

        public List<String> placeholders() {
            Pattern p = Pattern.compile("(\\$\\{\\s*(?<holder>[\\w\\d_\\.\\-]+)\\s*\\})");
            Matcher m = p.matcher(content);
            Set<String> set = Sets.newHashSet();
            while (m.find()) {
                String holder = m.group("holder");
                set.add(holder);
            }
            return Lists.newArrayList(set);
        }


        @Override
        public String toString() {
            return content;
        }

        public String toString(List<Object> args) {
            return regexAndFill(args);
        }


        public String toString(Map<String, Object> kwargs) {
            return regexAndFill(kwargs);
        }

        public String toString(String json) {
            if (json == null) return content;
            try {
                json = json.trim();
                if (json.startsWith("{")) {
                    Map<String, Object> map = JSON.parseObject(json, new TypeReference<Map<String, Object>>() {});
                    return regexAndFill(map);
                } else if (json.startsWith("[")) {
                    List<Object> list = JSON.parseArray(json, Object.class);
                    return regexAndFill(list);
                } else {
                    return content;
                }
            } catch (Exception e) {
                return content;
            }
        }

        public String regexAndFill(List<Object> args) {
            if (neededFill() && args != null && args.size() > 0) {
                String newcontent = content;
                int len = args.size();
                for (int i = 0; i < len; ++i) {
                    Object obj = args.get(i);
                    if (obj == null) continue;
                    String val = obj instanceof Date ? SDF.format(obj) : obj.toString();
                    newcontent = newcontent.replaceAll("\\$\\{\\s*" + i + "\\s*\\}", val);
                }
                return newcontent;
            } else {
                return content;
            }
        }

        public String regexAndFill(Map<String, Object> kwargs) {
            if (neededFill() && kwargs != null && kwargs.size() > 0) {
                String newcontent = content;
                List<String> holders = placeholders();
                for (String holder : holders) {
                    if (!kwargs.containsKey(holder)) continue;
                    Object obj = kwargs.get(holder);
                    String val = obj instanceof Date ? SDF.format(obj) : obj.toString();
                    newcontent = newcontent.replaceAll("\\$\\{\\s*" + holder + "\\s*\\}", val);
                }
                return newcontent;
            } else {
                return content;
            }
        }
    }
