require "jekyll"

# Migrated WordPress content links to root-relative paths like /images/wp/...
# When the site is served from a subpath (e.g. a github.io project page),
# prefix those links with the baseurl. Does nothing when baseurl is empty.
Jekyll::Hooks.register [:pages, :documents], :post_render do |doc|
  baseurl = doc.site.config["baseurl"].to_s.chomp("/")
  next if baseurl.empty? || !doc.output_ext.to_s.start_with?(".htm")
  prefix = Regexp.escape(baseurl)
  doc.output = doc.output.gsub(%r{(href|src)="/(?!/)(?!#{prefix[1..]}/)}) { "#{$1}=\"#{baseurl}/" }
end
