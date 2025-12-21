const std = @import("std");

const Range = struct { start: u64, end: u64 };

fn split_id_range(id_range: []const u8) !Range {
    var range_iter = std.mem.splitAny(u8, id_range, "-");
    const start_str = range_iter.first();
    const end_str = range_iter.rest();
    const start = try std.fmt.parseInt(u64, start_str, 10);
    const end = try std.fmt.parseInt(u64, end_str, 10);

    const range: Range = .{
        .start = start,
        .end = end,
    };
    return range;
}

pub fn main() !void {
    const file = try std.fs.cwd().openFile("5/input.txt", .{ .mode = .read_only });
    defer file.close();

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const file_size: u64 = (try file.stat()).size;
    const buffer: []u8 = try allocator.alloc(u8, file_size);
    defer allocator.free(buffer);

    _ = try file.read(buffer);

    var iter = std.mem.splitAny(u8, buffer, "\n");

    const fresh_id_ranges = try allocator.alloc(Range, 10000);
    defer allocator.free(fresh_id_ranges);

    var i_possible: usize = 0;
    var i_actual: usize = 0;
    var id_range: bool = true;
    while (iter.next()) |id_or_id_range| {
        const empty_line: bool = std.mem.eql(u8, id_or_id_range, "");
        if (empty_line) {
            id_range = false;
        } else {
            if (id_range & !empty_line) {
                const range = try split_id_range(id_or_id_range);
                fresh_id_ranges[i_possible] = range;
                i_possible += 1;
            } else {
                const id = try std.fmt.parseInt(u64, id_or_id_range, 10);
                for (fresh_id_ranges) |range| {
                    if (id >= range.start and id <= range.end) {
                        i_actual += 1;
                        break;
                    }
                }
            }
        }
    }

    std.debug.print("{any}\n", .{i_actual});
}
