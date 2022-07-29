my $file="data.txt";
open(FH, "<", $file) or die ("error");
my %key_hash;
while($line=<FH>)
{
@arr=split(" ",$line);

push @{$key_hash{$arr[0]}},$arr[1];
}
for $key (keys (%key_hash))
{ 
$data="";
@key_value=@{$key_hash{$key}};


 if (scalar(@key_value>1))
	 {
		 $data=join(",",@key_value);
			print "$key $data \n";
			break;
	 }
	 else
	 {$data=$key_value[0];
	print "$key $data \n";
	break;
	 }
	  
} 



 
 
 
 
 
 
 


