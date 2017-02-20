module Jekyll
  module DateSort
    require 'date'

    def date_sort(collection, field)
      collection.sort_by do |item|
        Date.parse(item.data[field])
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::DateSort)
