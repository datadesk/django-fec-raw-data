require 'fech'
require 'csv'

begin
    filing_no = ARGV[0]
    base_dir = ARGV[1]

    # Where to store .fec files
    raw_path = File.join(base_dir, 'raw')
    raw_dir = Dir.open(raw_path)

    filing = Fech::Filing.new(filing_no, :download_dir =>  raw_dir, :csv_parser => Fech::CsvDoctor)
    filing.download

    # Strip "N" and "A" from form type
    form_type = filing.form_type.gsub(/[AN"]/, '')

    # Create directory for these filings if it doesn't exist
    dir_path = File.join(base_dir, form_type)
    Dir.mkdir(dir_path) unless File.exists?(dir_path)

    # Create csv for summary
    path = File.join(base_dir, form_type, filing_no + '.csv')
    CSV.open(path, 'w') do |csv|
        # Add filing number, amendment id, amendment number
        csv << ['filing_no','report_id', 'report_number'] + filing.summary.keys
        csv << [filing_no, filing.amends, filing.header.report_number] + filing.summary.values
    end

    line_types = {
        'sa' => /sa/, # Contributions
        'sb' => /sb/, # Disbursements
        'sc' => /sc/, # Loans
        'sd' => /sd/, # Debts
        'se' => /se/, # Independent expenditures
        'sf' => /sf/, # Coordinated expenditures
    }

    # Create separate csv files for each line type
    line_types.each do |type, expr|
        rows = filing.enum_for(:rows_like, expr)
        if rows.any?
            # Make sure the directory exists
            dir_path = File.join(base_dir, type)
            Dir.mkdir(dir_path) unless File.exists?(dir_path)

            path = File.join(dir_path, filing_no + '_' + type + '.csv')
            CSV.open(path, 'w') do |csv|
                # Dump the header
                csv << ['filing_no'] + rows.peek.keys
                rows.each do |row|
                    csv << [filing_no] + row.values
                end
            end
        end
    end
    puts 'SUCCESS'
rescue
    puts 'ERROR'
end
