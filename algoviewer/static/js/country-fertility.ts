import * as fs from "fs";
import * as path from "path";
import { parse } from "csv-parse";
import { Console } from "console";

/**
 * Describes a data entry for the fertility data.
 * @property region: string  - geographical region of the country (e.g. South Asia)
 * @property country: string - name of the country
 * @property fertility: number - births/woman (source - https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependencies_by_total_fertility_rate)
 * @property rank: number - fertility rank when compared with all other counties in the data set
 * @property GDP_PPP: number - "gross domestic product based on purchasing power parity" of the country
 */
type CountryFertility = {
    region: string;
    country: string;
    fertility: number;
    rank: number;
    pop: number;
    GDP_PPP: number;
};

/**
 * Reads the fertility data csv into an Array
 * @param isSilent: boolean = set to false to print error messages etc.
 * @returns an Array of CountryFertility objects based on the data set
 */
function readCsv(isSilent = true): Array<CountryFertility> {
    const filePath: string = path.resolve(__dirname, "../data/fertility.csv");
    const content: Array<CountryFertility> = [];

    fs.createReadStream(filePath)
        .pipe(parse({ delimiter: ',', from_line: 2}))
        .on("data", function (row) {  // if the row is data
            content.push({
                region: row[0],
                country: row[1],
                fertility: <number> row[2],
                // skipping row 4 (rankWiki)
                rank: <number> row[4],
                pop: <number> row[5],
                GDP_PPP: <number> row[6]
            });
        })
        .on("end", function () {  // what happens when there is no more data
            if (!isSilent) console.log("Finished loading data");
        })
        .on("error", function (error) {
            if (!isSilent) console.log(error.message);
        });
    return content;
}
readCsv();