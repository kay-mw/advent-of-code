use std::fs;
use std::str::Chars;

// X-1, Y-1
// X, Y-1
// X+1, Y-1
//
// X-1, Y
// X+1, Y
//
// X-1, Y+1
// X, Y+1
// X+1, Y+1

fn increment_rolls_if_paper(value: char, mut rolls: usize) -> usize {
    if value == '@' {
        rolls += 1;
    }

    return rolls;
}

fn count_adjacent_rolls(
    matrix: Vec<Chars>,
    row_index: usize,
    col_index: usize,
    max_row_index: usize,
    max_col_index: usize,
) -> usize {
    let mut rolls: usize = 0;
    if row_index < max_row_index {
        if col_index > 0 {
            if let Some(bottom_left) = matrix[row_index + 1].clone().nth(col_index - 1) {
                rolls = increment_rolls_if_paper(bottom_left, rolls);
                // println!("Bottom left: {rolls}")
            }
        }
        if let Some(bottom_middle) = matrix[row_index + 1].clone().nth(col_index) {
            rolls = increment_rolls_if_paper(bottom_middle, rolls);
            // println!("Bottom middle: {rolls}")
        }
        if col_index < max_col_index {
            if let Some(bottom_right) = matrix[row_index + 1].clone().nth(col_index + 1) {
                rolls = increment_rolls_if_paper(bottom_right, rolls);
                // println!("Bottom right: {rolls}")
            }
        }
    }

    if col_index > 0 {
        if let Some(left) = matrix[row_index].clone().nth(col_index - 1) {
            rolls = increment_rolls_if_paper(left, rolls);
            // println!("Left: {rolls}")
        }
    }
    if col_index < max_col_index {
        if let Some(right) = matrix[row_index].clone().nth(col_index + 1) {
            rolls = increment_rolls_if_paper(right, rolls);
            // println!("Right: {rolls}")
        }
    }

    if row_index > 0 {
        if col_index > 0 {
            if let Some(top_left) = matrix[row_index - 1].clone().nth(col_index - 1) {
                rolls = increment_rolls_if_paper(top_left, rolls);
                // println!("Top left: {rolls}");
            }
        }
        if let Some(top_middle) = matrix[row_index - 1].clone().nth(col_index) {
            rolls = increment_rolls_if_paper(top_middle, rolls);
            // println!("Top middle: {rolls}");
        }
        if col_index < max_col_index {
            if let Some(top_right) = matrix[row_index - 1].clone().nth(col_index + 1) {
                rolls = increment_rolls_if_paper(top_right, rolls);
                // println!("Top right: {rolls}");
            }
        }
    }

    return rolls;
}

fn main() {
    let contents: String = fs::read_to_string("4/input.txt").expect("Failed to read the file");

    let mut parts: Vec<&str> = contents.split("\n").collect();
    parts.remove(parts.len() - 1);
    let mut parts_str: Vec<String> = parts.iter().map(|x| x.to_string()).collect();

    let mut total_liftable = 0;
    loop {
        let mut matrix: Vec<_> = parts_str.iter().map(|x| x.chars()).collect();

        let mut liftable = 0;
        let mut row_index = 0;
        let mut liftable_positions: Vec<(usize, usize)> = Vec::new();
        for row in matrix.clone() {
            // println!("\nProcessing...");
            let mut col_index = 0;
            for cell in row.clone() {
                if cell == '@' {
                    // println!("row_pos: {row_index}, col_pos: {col_index}");
                    let rolls: usize = count_adjacent_rolls(
                        matrix.clone(),
                        row_index,
                        col_index,
                        row.clone().count() - 1,
                        matrix.len(),
                    );
                    // println!("Adjacent rolls: {rolls}\n");
                    if rolls < 4 {
                        liftable += 1;
                        liftable_positions.push((row_index, col_index))
                    }
                }
                col_index += 1;
            }
            row_index += 1;
        }

        for position in liftable_positions.clone() {
            let row_index: usize = position.0;
            let col_index: usize = position.1;
            parts_str[row_index].replace_range(col_index..col_index + 1, ".");
        }

        // println!("{:#?}", parts_str);
        // println!("{liftable}");

        total_liftable += liftable;

        if liftable == 0 {
            break;
        }
    }

    println!("{total_liftable}");
}
