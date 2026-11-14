from dataclasses import asdict, dataclass

@dataclass(frozen=True)
class ArrayReport:
    shape: tuple[int,...]
    dtype:str
    size: int
    nan_count:int
    infinite_count: int
    constant_columns: tuple[int,...]
    duplicate_rows: int
    
    @property
    def issues(self)->list[str]:
        findings=[]
        if self.nan_count:
            findings.append(
                f"Found {self.nan_count} NaN value(s)"
            )
        
        if self.infinite_count:
            findings.append(
                f"Found {self.infinite_count} infinite value(s)"
            )
        
        if self.constant_columns:
            findings.append(
                "Constant columns are:"+ " ".join(map(str, self.constant_columns))+ " "  
            )
        
        if self.duplicate_rows:
            findings.append(
                f"Found{self.duplicate_rows} duplicate row(s)"
            )

        return findings
    
    def to_dict(self)->dict:
        return asdict(self) 
    
    def summary(self)->str:
        lines=[
            "~"*25,
            f"Shape: {self.shape}",
            f"Data type: {self.dtype}",
            f"Elements: {self.size}",
            f"NaN values: {self.nan_count}",
            f"Infinite values: {self.infinite_count}",
        ]
        if self.constant_columns:
            lines.append(
                f"Constant columns: {self.constant_columns}"
            )

        lines.append(f"Duplicate rows: {self.duplicate_rows}")

        if self.issues:
            lines.append("")
            lines.append("Findings:")
            lines.extend(f"- {issue}" for issue in self.issues)
        else:
            lines.append("")
            lines.append("No configured issues detected.")

        return "\n".join(lines)